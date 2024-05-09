from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import generic

from manager.models import Worker
from manager.services import get_workers


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("username")

        context["segment"] = ["search", "workers"]
        context["search_name"] = "username"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search worker"

        return context

    def get_queryset(self) -> QuerySet[Worker]:
        search_value = self.request.GET.get("username")

        return get_workers(username=search_value)
