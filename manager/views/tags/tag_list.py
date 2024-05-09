from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import generic

from manager.models import Tag
from manager.services import get_project_tags, get_project_by_id


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TagListView, self).get_context_data(**kwargs)
        search_value = self.request.GET.get("tag-name")

        context["segment"] = ["search"]
        context["search_name"] = "tag-name"
        context["search_value"] = search_value if search_value else ""
        context["search_placeholder"] = "Search tags"
        context["project"] = get_project_by_id(self.kwargs["pk"])

        return context

    def get_queryset(self) -> QuerySet[Tag]:
        search_value = self.request.GET.get("tag-name")

        return get_project_tags(project_id=self.kwargs["pk"], tag_name=search_value)
