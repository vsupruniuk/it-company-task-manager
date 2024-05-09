from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import WorkerForm
from manager.models import Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("manager:worker-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerCreateView, self).get_context_data(**kwargs)

        context["segment"] = ["workers"]

        return context
