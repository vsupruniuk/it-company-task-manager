from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.models import Project, Task
from manager.services import get_projects_with_tasks


class GetProjectsWithTasksTests(TestCase):
    def setUp(self) -> None:
        self.project_youtube = Project.objects.create(
            name="YouTube", start_date=datetime(2024, 1, 1), budget=100_000_000
        )
        self.project_twitch = Project.objects.create(
            name="Twitch", start_date=datetime(2024, 1, 1), budget=150_000_000
        )
        self.project_instagram = Project.objects.create(
            name="Instagram", start_date=datetime(2024, 1, 1), budget=125_000_000
        )
        self.project_facebook = Project.objects.create(
            name="Facebook", start_date=datetime(2024, 1, 1), budget=200_000_000
        )
        self.project_whatsapp = Project.objects.create(
            name="WhatsApp", start_date=datetime(2024, 1, 1), budget=75_000_000
        )

        self.worker_tony = get_user_model().objects.create(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )
        self.worker_bruce = get_user_model().objects.create(
            first_name="Bruce",
            last_name="Banner",
            username="b.banner",
            password="Qwerty12345!",
        )
        self.worker_thor = get_user_model().objects.create(
            first_name="Thor",
            last_name="Odinson",
            username="t.odinson",
            password="Qwerty12345!",
        )
        self.worker_steve = get_user_model().objects.create(
            first_name="Steve",
            last_name="Rogers",
            username="s.rogers",
            password="Qwerty12345!",
        )

        self.task_youtube_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=self.project_youtube,
        )
        self.task_youtube_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=self.project_youtube,
            is_completed=True,
        )
        self.task_twitch_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=self.project_twitch,
        )
        self.task_twitch_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=self.project_twitch,
            is_completed=True,
        )
        self.task_instagram_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=self.project_instagram,
        )
        self.task_instagram_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=self.project_instagram,
            is_completed=True,
        )
        self.task_facebook_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=self.project_facebook,
        )
        self.task_facebook_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=self.project_facebook,
            is_completed=True,
        )

        self.task_youtube_deploy_db.assignees.set((self.worker_tony,))
        self.task_youtube_create_design.assignees.set((self.worker_tony,))

        self.task_twitch_deploy_db.assignees.set((self.worker_bruce,))
        self.task_twitch_create_design.assignees.set((self.worker_bruce,))

        self.task_instagram_deploy_db.assignees.set((self.worker_thor,))
        self.task_instagram_create_design.assignees.set((self.worker_thor,))

        self.task_facebook_deploy_db.assignees.set((self.worker_steve,))
        self.task_facebook_create_design.assignees.set((self.worker_steve,))

    def test_each_project_has_only_own_tasks(self) -> None:
        projects = get_projects_with_tasks(None)

        for project in projects:
            for task in project.tasks.all():
                self.assertEqual(task.project.id, project.id)

    def test_should_count_total_tasks_for_each_project(self) -> None:
        total_tasks = 2

        projects = get_projects_with_tasks(None)

        for project in projects:
            self.assertEqual(project.total_tasks, total_tasks)

    def test_should_count_completed_tasks_count_for_each_project(self) -> None:
        completed_tasks_count = 1

        projects = get_projects_with_tasks(None)

        for project in projects:
            self.assertEqual(project.completed_tasks_count, completed_tasks_count)

    def test_should_count_uncompleted_tasks_count_for_each_project(self) -> None:
        uncompleted_tasks_count = 1

        projects = get_projects_with_tasks(None)

        for project in projects:
            self.assertEqual(project.uncompleted_tasks_count, uncompleted_tasks_count)

    def test_should_count_completed_tasks_percentage_for_each_project(self) -> None:
        completed_tasks_percentage = 50

        projects = get_projects_with_tasks(None)

        for project in projects:
            self.assertEqual(
                project.completed_tasks_percentage, completed_tasks_percentage
            )

    def test_should_count_uncompleted_tasks_percentage_for_each_project(self) -> None:
        uncompleted_tasks_percentage = 50

        projects = get_projects_with_tasks(None)

        for project in projects:
            self.assertEqual(
                project.uncompleted_tasks_percentage, uncompleted_tasks_percentage
            )

    def test_should_return_projects_with_one_or_more_tasks(self) -> None:
        projects = get_projects_with_tasks(None)

        self.assertNotIn(self.project_whatsapp, projects)

    def test_should_filter_projects_by_name_if_name_provided(self) -> None:
        projects = get_projects_with_tasks("you")

        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0].name, self.project_youtube.name)
