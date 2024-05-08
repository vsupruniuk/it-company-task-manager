from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import PositionForm
from manager.models import Position
from manager.services import get_position_with_team


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PositionUpdateView, self).get_context_data(**kwargs)

        context["team"] = get_position_with_team(self.kwargs["pk"]).team

        return context

    def get_success_url(self) -> str:
        position = get_position_with_team(self.kwargs["pk"])

        return reverse_lazy("manager:position-list", kwargs={"pk": position.team.pk})
