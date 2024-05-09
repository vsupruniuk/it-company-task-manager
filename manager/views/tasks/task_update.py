from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task
from manager.services import get_full_task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskUpdateView, self).get_context_data(**kwargs)

        context["project"] = get_full_task(self.kwargs["pk"]).project

        return context

    def get_success_url(self) -> str:
        task = get_full_task(self.kwargs["pk"])

        return reverse_lazy("manager:task-list", kwargs={"pk": task.project.pk})
