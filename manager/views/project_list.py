from django.views import generic

from manager.models import Project


class ProjectListView(generic.ListView):
    model = Project
    context_object_name = "project_list"
