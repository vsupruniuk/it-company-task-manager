from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Team


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("manager:team-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TeamDeleteView, self).get_context_data(**kwargs)

        context["segment"] = ["teams"]

        return context
