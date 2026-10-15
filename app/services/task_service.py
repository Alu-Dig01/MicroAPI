"""Business rules for task management."""

from __future__ import annotations

from uuid import UUID

from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import Priority, PriorityAdvisor


class TaskService:
    """Coordinates task persistence and priority suggestions."""

    def __init__(
        self,
        repository: TaskRepository,
        priority_advisor: PriorityAdvisor,
    ) -> None:
        """Initialize the service dependencies."""
        self._repository = repository
        self._priority_advisor = priority_advisor
        self._priority_suggestions: dict[UUID, Priority] = {}

    def create(self, task: TaskCreate) -> TaskOut:
        """Create a task and calculate its priority suggestion."""
        created_task = self._repository.create(task)
        self._priority_suggestions[created_task.id] = self._suggest_priority(
            created_task,
        )
        return created_task

    def list(self) -> list[TaskOut]:
        """Return all tasks."""
        return self._repository.list()

    def get_by_id(self, task_id: UUID) -> TaskOut | None:
        """Return a task by identifier."""
        return self._repository.get_by_id(task_id)

    def update(self, task_id: UUID, task: TaskUpdate) -> TaskOut | None:
        """Update a task and refresh its priority suggestion."""
        updated_task = self._repository.update(task_id, task)
        if updated_task is None:
            return None

        self._priority_suggestions[task_id] = self._suggest_priority(updated_task)
        return updated_task

    def delete(self, task_id: UUID) -> bool:
        """Delete a task and its associated suggestion."""
        was_deleted = self._repository.delete(task_id)
        if was_deleted:
            self._priority_suggestions.pop(task_id, None)
        return was_deleted

    def get_suggested_priority(self, task_id: UUID) -> Priority | None:
        """Return the current priority suggestion for a task."""
        return self._priority_suggestions.get(task_id)

    def _suggest_priority(self, task: TaskOut) -> Priority:
        """Delegate priority calculation to the advisor."""
        return self._priority_advisor.suggest(task.title, task.description)
