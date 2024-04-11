from django.urls import path

from manager.views import (
    index,
    my_tasks,
    ProjectListView,
    TeamListView,
    WorkerListView,
    ProjectTaskListView,
    ProjectTaskUpdateView,
    ProjectTaskDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("my-tasks/", my_tasks, name="my-tasks"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path(
        "projects/<int:pk>/tasks",
        ProjectTaskListView.as_view(),
        name="project-task-list",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/update",
        ProjectTaskUpdateView.as_view(),
        name="project-task-update",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/delete",
        ProjectTaskDeleteView.as_view(),
        name="project-task-delete",
    ),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
]

app_name = "manager"
