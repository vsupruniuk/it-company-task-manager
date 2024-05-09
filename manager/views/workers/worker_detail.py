from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Worker
from manager.services import get_worker


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerDetailView, self).get_context_data(**kwargs)

        context["segment"] = ["workers"]

        return context

    def get_object(self, queryset=None) -> Worker:
        return get_worker(self.kwargs["pk"])
