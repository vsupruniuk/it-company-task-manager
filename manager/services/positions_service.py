from django.db.models import QuerySet

from manager.models import Position


def get_team_positions(
    team_id: int, position_name: str | None = None
) -> QuerySet[Position]:
    queryset = Position.objects.select_related("team").filter(team_id=team_id)

    if position_name:
        queryset = queryset.filter(name__icontains=position_name)

    return queryset
