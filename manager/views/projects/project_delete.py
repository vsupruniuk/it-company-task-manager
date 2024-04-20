from django.views import generic

from manager.models import Project


class ProjectDeleteView(generic.DeleteView):
    model = Project
