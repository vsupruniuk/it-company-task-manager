from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Team
from manager.services import get_team


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TeamDetailView, self).get_context_data(**kwargs)

        context["segment"] = ["teams"]

        return context

    def get_object(self, queryset=None) -> Team:
        return get_team(self.kwargs["pk"])
