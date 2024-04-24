from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Project


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        context["segment"] = ["projects"]

        return context
