from django.db.models import QuerySet

from manager.models import TaskType


def get_project_task_types(
    prj_id: int, task_name: str | None = None
) -> QuerySet[TaskType]:
    queryset = TaskType.objects.select_related("project").filter(project_id=prj_id)

    if task_name:
        queryset = queryset.filter(name__icontains=task_name)

    return queryset
