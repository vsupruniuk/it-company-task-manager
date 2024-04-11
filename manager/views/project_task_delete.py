from django.views import generic

from manager.models import Task


class ProjectTaskDeleteView(generic.DeleteView):
    model = Task
