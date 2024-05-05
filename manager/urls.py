from django.urls import path

from manager.views import (
    index,
    my_tasks,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TagListView,
    TagDetailView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
    PositionListView,
    PositionDetailView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    TaskDeleteView,
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
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "projects/<int:pk>/tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/",
        TaskDetailView.as_view(),
        name="task-detail",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "projects/<int:pk>/tasks/<int:id>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path("projects/<int:pk>/tags/", TagListView.as_view(), name="tag-list"),
    path(
        "projects/<int:pk>/tags/<int:id>/", TagDetailView.as_view(), name="tag-detail"
    ),
    path("projects/<int:pk>/tags/create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "projects/<int:pk>/tags/<int:id>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "projects/<int:pk>/tags/<int:id>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "projects/<int:pk>/task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "projects/<int:pk>/task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    path(
        "projects/<int:pk>/task-types/<int:id>/",
        TaskTypeDetailView.as_view(),
        name="task-type-detail",
    ),
    path(
        "projects/<int:pk>/task-types/<int:id>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "projects/<int:pk>/task-types/<int:id>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("teams/create/", TeamCreateView.as_view(), name="team-create"),
    path("teams/<int:pk>/update/", TeamUpdateView.as_view(), name="team-update"),
    path("teams/<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
    path("teams/<int:pk>/positions/", PositionListView.as_view(), name="position-list"),
    path(
        "teams/<int:pk>/positions/<int:id>/",
        PositionDetailView.as_view(),
        name="position-detail",
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
]

app_name = "manager"
