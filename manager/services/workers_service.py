from django.db.models import QuerySet

from manager.models import Worker


def get_workers(username: str | None = None) -> QuerySet[Worker]:
    queryset = Worker.objects.select_related("position", "team")

    if username:
        queryset = queryset.filter(username__icontains=username)

    return queryset


def get_worker(worker_id: int) -> Worker:
    return Worker.objects.select_related("position", "team").get(id=worker_id)
