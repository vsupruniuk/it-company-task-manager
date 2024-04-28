from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import TaskType


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_confirm_delete.html"
    context_object_name = "task_type"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskTypeDeleteView, self).get_context_data(**kwargs)

        context["project_id"] = self.kwargs["pk"]

        return context

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:task-type-list", kwargs={"pk": project_pk})
