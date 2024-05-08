from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import TaskType
from manager.services import get_task_type_with_project


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "manager/task_type_confirm_delete.html"
    context_object_name = "task_type"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskTypeDeleteView, self).get_context_data(**kwargs)

        context["project"] = get_task_type_with_project(self.kwargs["pk"]).project

        return context

    def get_success_url(self) -> str:
        task_type = get_task_type_with_project(self.kwargs["pk"])

        return reverse_lazy(
            "manager:task-type-list", kwargs={"pk": task_type.project.pk}
        )
