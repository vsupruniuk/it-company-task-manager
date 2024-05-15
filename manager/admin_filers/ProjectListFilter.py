from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from manager.models import Project


class ProjectListFilter(admin.SimpleListFilter):
    title = "project"
    parameter_name = "project"

    def lookups(self, request: HttpRequest, model_admin: Project) -> list[tuple]:
        return [(project.id, project.name) for project in Project.objects.all()]

    def queryset(
        self, request: HttpRequest, queryset: QuerySet[Project]
    ) -> QuerySet[Project]:
        project_id = self.value()

        if project_id:
            return queryset.filter(id=project_id)
