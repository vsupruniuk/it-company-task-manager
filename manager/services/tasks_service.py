from django.db.models import QuerySet

from manager.models import Task


def get_project_tasks(project_id: int, task_name: str | None = None) -> QuerySet[Task]:
    queryset = Task.objects.select_related("project").filter(project_id=project_id)

    if task_name:
        queryset = queryset.filter(name__icontains=task_name)

    return queryset
