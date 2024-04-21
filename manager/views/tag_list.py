from django.views import generic

from manager.models import Tag


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
