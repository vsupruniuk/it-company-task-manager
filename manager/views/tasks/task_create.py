from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task, Project


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "manager/task_form.html"
    form_class = TaskForm

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:task-list", kwargs={"pk": project_pk})

    def form_valid(self, form: TaskForm) -> HttpResponseRedirect:
        project_id = self.kwargs.get("pk")

        form.instance.project = get_object_or_404(Project, pk=project_id)

        return super().form_valid(form)

    def form_invalid(self, form: TaskForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))
