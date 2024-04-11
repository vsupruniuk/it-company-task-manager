from django.views import generic

from manager.models import Task


class ProjectTaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
