from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from manager.models import Team


class TeamListFilter(admin.SimpleListFilter):
    title = "team"
    parameter_name = "team"

    def lookups(self, request: HttpRequest, model_admin: Team) -> list[tuple]:
        return [(team.id, team.name) for team in Team.objects.all()]

    def queryset(
        self, request: HttpRequest, queryset: QuerySet[Team]
    ) -> QuerySet[Team]:
        team_id = self.value()

        if team_id:
            return queryset.filter(id=team_id)
