from typing import Any

from django.contrib import admin
from django.db.models import QuerySet

from manager.models import Team


class TeamListFilter(admin.SimpleListFilter):
    title = "team"
    parameter_name = "team"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple]:
        return [(team.id, team.name) for team in Team.objects.all()]

    def queryset(self, request: Any, queryset: QuerySet[Team]) -> QuerySet[Team]:
        team_id = self.value()

        if team_id:
            return queryset.filter(id=team_id)
