"""Modelo de dados para tarefas."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class Task(BaseModel):
    """Representa uma tarefa da aplicação."""

    id: UUID | None = Field(
        default=None,
        description="Identificador único da tarefa; opcional durante a criação.",
    )
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Título obrigatório da tarefa, entre 3 e 100 caracteres.",
    )
    description: str | None = Field(
        default=None,
        description="Descrição opcional da tarefa.",
    )
    status: bool = Field(
        default=False,
        description="Indica se a tarefa está concluída.",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Data e hora UTC de criação da tarefa.",
    )
