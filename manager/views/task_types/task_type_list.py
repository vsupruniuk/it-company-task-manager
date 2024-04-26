from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import generic

from manager.models import TaskType
from manager.services import get_project_task_types


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("task-type-name")

        context["segment"] = ["search"]
        context["search_name"] = "task-type-name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search task types"

        return context

    def get_queryset(self) -> QuerySet[TaskType]:
        search_value = self.request.GET.get("task-type-name")

        return get_project_task_types(self.kwargs["pk"], task_name=search_value)
