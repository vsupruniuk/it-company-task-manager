from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Worker


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:worker-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerDeleteView, self).get_context_data(**kwargs)

        context["segment"] = ["workers"]

        return context
