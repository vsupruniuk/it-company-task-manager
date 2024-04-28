from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import TaskType
from manager.services import get_task_type_with_project


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type"

    def get_object(self, queryset=None) -> TaskType:
        return get_task_type_with_project(self.kwargs["pk"])
