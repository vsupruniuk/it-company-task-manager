from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Project


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("manager:project-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ProjectDeleteView, self).get_context_data(**kwargs)

        context["segment"] = ["projects"]

        return context
