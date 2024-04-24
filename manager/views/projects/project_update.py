from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import ProjectFrom
from manager.models import Project


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectFrom
    success_url = reverse_lazy("manager:project-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)

        context["segment"] = ["projects"]

        return context
