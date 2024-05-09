from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.admin_filers import TeamListFilter, ProjectListFilter
from manager.models import Position, TaskType, Tag, Worker, Task, Project, Team


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "team")
    list_filter = (TeamListFilter,)
    search_fields = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "project")
    list_filter = (ProjectListFilter,)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "project")
    list_filter = (ProjectListFilter,)
    search_fields = ("name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "team")
    list_filter = UserAdmin.list_filter + ("position", "team")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("team", "position")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional Info", {"fields": ("team", "position")}),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "deadline",
        "is_completed",
        "priority",
        "reporter",
        "project",
    )
    list_filter = (
        "deadline",
        "is_completed",
        "priority",
        "task_type",
        "reporter",
        ProjectListFilter,
        "assignees",
        "tags",
    )
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "budget")
    list_filter = ("start_date",)
    search_fields = ("name",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "team_lead")
    list_filter = ("team_lead", ProjectListFilter)
    search_fields = ("name",)
