from django.views import generic

from manager.models import Project


class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = "__all__"
