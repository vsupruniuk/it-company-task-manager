from django.db.models import QuerySet
from django.views import generic

from manager.models import Project
from manager.services import get_all_projects
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ProjectListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("project-name")

        context["segment"] = ["projects", "search"]
        context["search_name"] = "project-name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search projects"

        return context

    def get_queryset(self) -> QuerySet[Project]:
        project_name = self.request.GET.get("project-name")
        queryset = get_all_projects(project_name)

        return queryset
