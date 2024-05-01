from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:task-list", kwargs={"pk": project_pk})
