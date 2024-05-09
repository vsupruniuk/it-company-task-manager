from django.db.models import QuerySet

from manager.models import Team


def get_teams(name: str | None = None) -> QuerySet[Team]:
    queryset = Team.objects.select_related("team_lead").prefetch_related("projects")

    if name:
        queryset = queryset.filter(name__icontains=name)

    return queryset


def get_team(team_id: int) -> Team:
    return (
        Team.objects.select_related("team_lead")
        .prefetch_related("projects")
        .get(id=team_id)
    )
