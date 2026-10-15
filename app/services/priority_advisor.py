"""Priority suggestions with a local heuristic and optional LLM enhancement."""

from __future__ import annotations

import logging
import os
from typing import Literal

Priority = Literal["low", "medium", "high"]

logger = logging.getLogger(__name__)


class PriorityAdvisor:
    """Suggest task priority without blocking the CRUD flow."""

    _HIGH_PRIORITY_TERMS = frozenset(
        {"blocker", "critical", "critico", "crítico", "urgent", "urgente"},
    )
    _LOW_PRIORITY_TERMS = frozenset(
        {"backlog", "later", "quando possivel", "quando possível", "someday"},
    )

    def __init__(
        self,
        *,
        timeout_seconds: float = 3.0,
        model: str | None = None,
    ) -> None:
        """Configure the optional provider call."""
        self._api_key = os.getenv("OPENAI_API_KEY")
        self._model = model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        self._timeout_seconds = timeout_seconds

    def suggest(self, title: str, description: str | None = None) -> Priority:
        """Return a priority suggestion, falling back safely when needed."""
        fallback = self._suggest_locally(title, description)
        if not self._api_key:
            return fallback

        try:
            return self._suggest_with_llm(title, description, fallback)
        except Exception:
            logger.warning(
                "Priority advisor provider call failed; using local fallback.",
                exc_info=True,
            )
            return fallback

    def _suggest_locally(self, title: str, description: str | None) -> Priority:
        """Apply a deterministic keyword-based heuristic."""
        text = f"{title} {description or ''}".casefold()
        if any(term in text for term in self._HIGH_PRIORITY_TERMS):
            return "high"
        if any(term in text for term in self._LOW_PRIORITY_TERMS):
            return "low"
        return "medium"

    def _suggest_with_llm(
        self,
        title: str,
        description: str | None,
        fallback: Priority,
    ) -> Priority:
        """Request an LLM suggestion with a bounded timeout."""
        try:
            from openai import APIError, APITimeoutError, OpenAI
        except ImportError:
            logger.warning("OpenAI SDK is unavailable; using local priority fallback.")
            return fallback

        prompt = (
            "Classify this task priority as exactly one of: low, medium, high. "
            "Return only the priority word.\n\n"
            f"Title: {title}\n"
            f"Description: {description or 'Not provided'}"
        )

        try:
            client = OpenAI(
                api_key=self._api_key,
                timeout=self._timeout_seconds,
                max_retries=0,
            )
            response = client.responses.create(
                model=self._model,
                input=prompt,
            )
        except APITimeoutError:
            logger.warning("Priority advisor timed out; using local priority fallback.")
            return fallback
        except APIError:
            logger.warning("Priority advisor provider error; using local fallback.")
            return fallback

        suggestion = response.output_text.strip().casefold()
        if suggestion == "low":
            return "low"
        if suggestion == "medium":
            return "medium"
        if suggestion == "high":
            return "high"

        logger.warning("Priority advisor returned an invalid priority; using fallback.")
        return fallback
