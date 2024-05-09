from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task
from manager.services import get_project_by_id


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskCreateView, self).get_context_data(**kwargs)

        context["project"] = get_project_by_id(self.kwargs["pk"])

        return context

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:task-list", kwargs={"pk": project_pk})

    def form_valid(self, form: TaskForm) -> HttpResponseRedirect:
        project_id = self.kwargs.get("pk")

        form.instance.project = get_project_by_id(project_id)

        return super().form_valid(form)

    def form_invalid(self, form: TaskForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))
