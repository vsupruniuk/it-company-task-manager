from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Task
from manager.services import get_projects_with_tasks


class PublicIndexViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:index")

    def test_index_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/")


class PrivateIndexViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:index")
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        project_youtube = Project.objects.create(
            name="YouTube", start_date=datetime(2024, 1, 1), budget=100_000_000
        )
        project_twitch = Project.objects.create(
            name="Twitch", start_date=datetime(2024, 1, 1), budget=150_000_000
        )
        project_instagram = Project.objects.create(
            name="Instagram", start_date=datetime(2024, 1, 1), budget=125_000_000
        )
        project_facebook = Project.objects.create(
            name="Facebook", start_date=datetime(2024, 1, 1), budget=200_000_000
        )
        project_whatsapp = Project.objects.create(
            name="WhatsApp", start_date=datetime(2024, 1, 1), budget=75_000_000
        )
        project_slack = Project.objects.create(
            name="Slack", start_date=datetime(2024, 1, 1), budget=500_000_000
        )

        worker_tony = get_user_model().objects.create(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )
        worker_bruce = get_user_model().objects.create(
            first_name="Bruce",
            last_name="Banner",
            username="b.banner",
            password="Qwerty12345!",
        )
        worker_thor = get_user_model().objects.create(
            first_name="Thor",
            last_name="Odinson",
            username="t.odinson",
            password="Qwerty12345!",
        )
        worker_steve = get_user_model().objects.create(
            first_name="Steve",
            last_name="Rogers",
            username="s.rogers",
            password="Qwerty12345!",
        )

        task_youtube_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=project_youtube,
        )
        task_youtube_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=project_youtube,
            is_completed=True,
        )
        task_twitch_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=project_twitch,
        )
        task_twitch_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=project_twitch,
            is_completed=True,
        )
        task_instagram_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=project_instagram,
        )
        task_instagram_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=project_instagram,
            is_completed=True,
        )
        task_facebook_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=project_facebook,
        )
        task_facebook_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=project_facebook,
            is_completed=True,
        )
        task_whatsapp_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=project_whatsapp,
        )
        task_whatsapp_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=project_whatsapp,
            is_completed=True,
        )
        task_slack_deploy_db = Task.objects.create(
            name="Deploy DB",
            deadline=datetime(2024, 4, 15),
            project=project_slack,
        )
        task_slack_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 15),
            project=project_slack,
            is_completed=True,
        )

        task_youtube_deploy_db.assignees.set((worker_tony,))
        task_youtube_create_design.assignees.set((worker_tony,))

        task_twitch_deploy_db.assignees.set((worker_bruce,))
        task_twitch_create_design.assignees.set((worker_bruce,))

        task_instagram_deploy_db.assignees.set((worker_thor,))
        task_instagram_create_design.assignees.set((worker_thor,))

        task_facebook_deploy_db.assignees.set((worker_steve,))
        task_facebook_create_design.assignees.set((worker_steve,))

        task_whatsapp_deploy_db.assignees.set((worker_steve,))
        task_whatsapp_create_design.assignees.set((worker_steve,))

        task_slack_deploy_db.assignees.set((worker_tony,))
        task_slack_create_design.assignees.set((worker_tony,))

    def test_should_display_list_of_projects_with_tasks(self) -> None:
        projects = get_projects_with_tasks(None)

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["page_obj"]), list(projects)[:5])

    def test_should_display_list_of_projects_with_pagination(self) -> None:
        projects = get_projects_with_tasks(None)

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["page_obj"]), list(projects)[5:])

    def test_should_display_list_of_projects_with_search(self) -> None:
        projects = get_projects_with_tasks("you")

        res = self.client.get(self.url + "?project-name=you")

        self.assertEqual(list(res.context["page_obj"]), list(projects)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/index.html")
