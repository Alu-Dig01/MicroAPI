"""Pydantic models for task API contracts."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Payload used to create a task."""

    title: str = Field(
        min_length=3,
        max_length=100,
        description="Task title.",
    )
    description: str | None = Field(
        default=None,
        description="Optional task description.",
    )
    status: bool = Field(
        default=False,
        description="Whether the task is completed.",
    )


class TaskUpdate(BaseModel):
    """Payload used to partially update a task."""

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Updated task title.",
    )
    description: str | None = Field(
        default=None,
        description="Updated task description.",
    )
    status: bool | None = Field(
        default=None,
        description="Updated completion status.",
    )


class TaskOut(BaseModel):
    """Task returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(description="Unique task identifier.")
    title: str = Field(description="Task title.")
    description: str | None = Field(description="Optional task description.")
    status: bool = Field(description="Whether the task is completed.")
    created_at: datetime = Field(description="UTC creation timestamp.")
