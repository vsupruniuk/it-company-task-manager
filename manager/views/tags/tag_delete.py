from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.models import Tag


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("manager:tag-list")

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TagDeleteView, self).get_context_data(**kwargs)

        context["project_id"] = self.kwargs["pk"]

        return context

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:tag-list", kwargs={"pk": project_pk})
