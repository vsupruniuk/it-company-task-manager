from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import generic

from manager.models import Position
from manager.services import get_team_positions


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PositionListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("position-name")

        context["segment"] = ["search"]
        context["search_name"] = "position-name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search position"
        context["team_id"] = self.kwargs["pk"]

        return context

    def get_queryset(self) -> QuerySet[Position]:
        search_value = self.request.GET.get("position-name")

        return get_team_positions(self.kwargs["pk"], position_name=search_value)
