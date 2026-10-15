"""HTTP routes for task management."""

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])

_task_service = TaskService(
    repository=TaskRepository(),
    priority_advisor=PriorityAdvisor(),
)


def get_task_service() -> TaskService:
    """Provide the task service dependency."""
    return _task_service


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, service: TaskServiceDep) -> TaskOut:
    """Create a task."""
    return service.create(task)


@router.get("", response_model=list[TaskOut])
def list_tasks(service: TaskServiceDep) -> list[TaskOut]:
    """List all tasks."""
    return service.list()


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: UUID, service: TaskServiceDep) -> TaskOut:
    """Get a task by identifier."""
    task = service.get_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found.",
        )
    return task


@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: UUID,
    task: TaskUpdate,
    service: TaskServiceDep,
) -> TaskOut:
    """Update a task by identifier."""
    updated_task = service.update(task_id, task)
    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found.",
        )
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID, service: TaskServiceDep) -> Response:
    """Delete a task by identifier."""
    if not service.delete(task_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found.",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
