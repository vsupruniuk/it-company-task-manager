from django.views import generic

from manager.models import Task


class ProjectTaskDetailView(generic.DetailView):
    model = Task
