from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import generic

from manager.models import Team
from manager.services import get_teams


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TeamListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("team-name")

        context["segment"] = ["search", "teams"]
        context["search_name"] = "team-name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search team"

        return context

    def get_queryset(self) -> QuerySet[Team]:
        search_value = self.request.GET.get("team-name")

        return get_teams(name=search_value)
