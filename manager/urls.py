from django.urls import path

from manager.views import (
    index,
    my_tasks,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TeamListView,
    WorkerListView,
    ProjectTaskListView,
    ProjectTaskDetailView,
    ProjectTaskUpdateView,
    ProjectTaskDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("my-tasks/", my_tasks, name="my-tasks"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path(
        "projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"
    ),
    path(
        "projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"
    ),
    path(
        "projects/<int:pk>/tasks/",
        ProjectTaskListView.as_view(),
        name="project-task-list",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/",
        ProjectTaskDetailView.as_view(),
        name="project-task-detail",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/update/",
        ProjectTaskUpdateView.as_view(),
        name="project-task-update",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/delete/",
        ProjectTaskDeleteView.as_view(),
        name="project-task-delete",
    ),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
]

app_name = "manager"
