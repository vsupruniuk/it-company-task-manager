from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Tag
from manager.services import get_tag_with_project


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TagDeleteView, self).get_context_data(**kwargs)

        context["project"] = get_tag_with_project(self.kwargs["pk"]).project

        return context

    def get_success_url(self) -> str:
        tag = get_tag_with_project(self.kwargs["pk"])

        return reverse_lazy("manager:tag-list", kwargs={"pk": tag.project.pk})
