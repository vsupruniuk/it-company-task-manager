from typing import Any

from django.contrib import admin
from django.db.models import QuerySet

from manager.models import Project


class ProjectListFilter(admin.SimpleListFilter):
    title = "project"
    parameter_name = "project"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple]:
        return [(project.id, project.name) for project in Project.objects.all()]

    def queryset(self, request: Any, queryset: QuerySet[Project]) -> QuerySet[Project]:
        project_id = self.value()

        if project_id:
            return queryset.filter(id=project_id)
