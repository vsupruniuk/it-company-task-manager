from django.db.models import QuerySet

from manager.models import TaskType


def get_project_task_types(
    project_id: int, task_type_name: str | None = None
) -> QuerySet[TaskType]:
    queryset = TaskType.objects.select_related("project").filter(project_id=project_id)

    if task_type_name:
        queryset = queryset.filter(name__icontains=task_type_name)

    return queryset


def get_task_type_with_project(task_type_id: int) -> TaskType:
    return TaskType.objects.select_related("project").get(id=task_type_id)


def create_task_type_for_project(project_id: int, name: str) -> None:
    TaskType.objects.create(name=name, project_id=project_id)
