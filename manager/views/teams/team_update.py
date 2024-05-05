from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TeamForm
from manager.models import Team


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("manager:team-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TeamUpdateView, self).get_context_data(**kwargs)

        context["segment"] = ["teams"]

        return context
