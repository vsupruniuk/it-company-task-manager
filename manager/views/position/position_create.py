from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import PositionForm
from manager.models import Position
from manager.services import create_position_for_team


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm

    def get_success_url(self) -> str:
        team_pk = self.kwargs["pk"]

        return reverse_lazy("manager:position-list", kwargs={"pk": team_pk})

    def form_valid(self, form: PositionForm) -> HttpResponseRedirect:
        create_position_for_team(
            team_id=self.kwargs["pk"], name=form.cleaned_data.get("name")
        )

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form: PositionForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))
