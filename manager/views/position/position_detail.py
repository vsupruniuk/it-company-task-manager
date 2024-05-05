from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Position
from manager.services import get_position_with_team


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "manager/position_detail.html"

    def get_object(self, queryset=None) -> Position:
        return get_position_with_team(self.kwargs["id"])
