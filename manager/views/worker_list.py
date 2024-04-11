from django.views import generic

from manager.models import Worker


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
