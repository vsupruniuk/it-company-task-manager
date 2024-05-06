from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import PositionForm
from manager.models import Position


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    form_class = PositionForm

    def get_success_url(self) -> str:
        team_pk = self.kwargs["pk"]

        return reverse_lazy("manager:position-list", kwargs={"pk": team_pk})
