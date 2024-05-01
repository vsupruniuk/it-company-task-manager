from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from manager.models import Task
from manager.services import get_full_task


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task

    def get_object(self, queryset=None) -> Task:
        return get_full_task(self.kwargs["id"])
