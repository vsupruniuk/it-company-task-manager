from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import generic

from manager.models import Task
from manager.services import get_project_tasks, get_project_by_id


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("task-name")

        context["segment"] = ["search"]
        context["search_name"] = "task-name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search task"
        context["project"] = get_project_by_id(self.kwargs["pk"])

        return context

    def get_queryset(self) -> QuerySet[Task]:
        search_value = self.request.GET.get("task-name")

        return get_project_tasks(project_id=self.kwargs["pk"], task_name=search_value)
