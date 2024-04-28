from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TagForm
from manager.models import Tag
from manager.services import create_tag_for_project


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    template_name = "manager/tag_form.html"
    form_class = TagForm

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:tag-list", kwargs={"pk": project_pk})

    def form_valid(self, form: TagForm) -> HttpResponseRedirect:
        create_tag_for_project(
            project_id=self.kwargs["pk"], name=form.cleaned_data.get("name")
        )

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form: TagForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))
