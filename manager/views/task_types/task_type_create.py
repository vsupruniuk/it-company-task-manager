from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskTypeForm
from manager.models import TaskType
from manager.services import create_task_type_for_project


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "manager/task_type_form.html"
    form_class = TaskTypeForm

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:task-type-list", kwargs={"pk": project_pk})

    def form_valid(self, form: TaskTypeForm) -> HttpResponseRedirect:
        create_task_type_for_project(
            project_id=self.kwargs["pk"], name=form.cleaned_data.get("name")
        )

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form: TaskTypeForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))
