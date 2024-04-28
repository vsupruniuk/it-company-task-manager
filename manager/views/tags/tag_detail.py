from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Tag
from manager.services import get_tag_with_project


class TagDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tag
    template_name = "manager/tag_detail.html"

    def get_object(self, queryset=None) -> Tag:
        return get_tag_with_project(self.kwargs["pk"])
