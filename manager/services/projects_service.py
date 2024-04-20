from django.db.models import (
    QuerySet,
    Prefetch,
    Count,
    Q,
    F,
    IntegerField,
)
from django.db.models.functions import Round

from manager.models import Project, Task


def get_all_projects(name: str | None = None) -> QuerySet[Project]:
    projects = Project.objects.all()

    if name:
        projects = projects.filter(name__icontains=name)

    return projects


def get_projects_with_tasks(project_name: str | None) -> QuerySet[Project]:
    projects = (
        Project.objects.prefetch_related(
            Prefetch("tasks", queryset=Task.objects.prefetch_related("assignees"))
        )
        .annotate(
            total_tasks=Count("tasks"),
            completed_tasks_count=Count("tasks", filter=Q(tasks__is_completed=True)),
            uncompleted_tasks_count=Count("tasks", filter=Q(tasks__is_completed=False)),
        )
        .annotate(
            completed_tasks_percentage=Round(
                100.0 * F("completed_tasks_count") / F("total_tasks"),
                output_field=IntegerField(),
            ),
            uncompleted_tasks_percentage=Round(
                100.0 * F("uncompleted_tasks_count") / F("total_tasks"),
                output_field=IntegerField(),
            ),
        )
    ).filter(total_tasks__gt=0)

    if project_name:
        projects = projects.filter(name__icontains=project_name)

    return projects
