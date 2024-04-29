from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TagForm
from manager.models import Tag


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    template_name = "manager/tag_form.html"
    form_class = TagForm

    def get_success_url(self) -> str:
        project_pk = self.kwargs["pk"]

        return reverse_lazy("manager:tag-list", kwargs={"pk": project_pk})
