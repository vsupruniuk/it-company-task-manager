from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TagForm
from manager.models import Tag
from manager.services import create_tag_for_project, get_project_by_id


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TagCreateView, self).get_context_data(**kwargs)

        context["project"] = get_project_by_id(self.kwargs["pk"])

        return context

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
