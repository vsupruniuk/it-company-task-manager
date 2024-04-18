from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from manager.models import Task


def update_user(
    user_id: int,
    email: str = None,
    username: str = None,
    first_name=None,
    last_name: str = None,
) -> get_user_model():
    user = get_user_model().objects.get(id=user_id)

    if email:
        user.email = email

    if username:
        user.username = username

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    user.save()

    return user


def get_user_tasks(
    user: get_user_model(), name: str = None, is_completed: bool | None = None
) -> QuerySet[Task]:
    tasks = (
        Task.objects.filter(assignees__in=[user])
        .select_related("project")
        .order_by("-updated_at")
    )

    if name:
        tasks = tasks.filter(name__icontains=name)

    if isinstance(is_completed, bool):
        tasks = tasks.filter(is_completed=is_completed)

    return tasks
