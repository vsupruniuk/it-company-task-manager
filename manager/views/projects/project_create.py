from django.views import generic

from manager.models import Project


class ProjectCreateView(generic.CreateView):
    model = Project
    fields = "__all__"
