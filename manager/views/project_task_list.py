from django.views import generic

from manager.models import Task


class ProjectTaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
