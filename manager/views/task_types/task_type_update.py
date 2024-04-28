from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskTypeForm
from manager.models import TaskType


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "manager/task_type_form.html"
    form_class = TaskTypeForm

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:task-type-list", kwargs={"pk": project_pk})
