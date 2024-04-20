from django.views import generic

from manager.models import Project


class ProjectDetailView(generic.DetailView):
    model = Project
