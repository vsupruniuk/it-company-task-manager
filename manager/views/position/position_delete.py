from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Position


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PositionDeleteView, self).get_context_data(**kwargs)

        context["team_id"] = self.kwargs["pk"]

        return context

    def get_success_url(self) -> str:
        team_pk = self.kwargs["pk"]

        return reverse_lazy("manager:position-list", kwargs={"pk": team_pk})
