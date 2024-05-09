from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Task
from manager.services import get_user_tasks


class PublicMyTasksViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:my-tasks")

    def test_my_tasks_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/my-tasks/")


class PrivateMyTasksViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:my-tasks")
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        task_create_db_structure = Task.objects.create(
            name="Create DB structure",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
            is_completed=True,
        )
        task_create_design = Task.objects.create(
            name="Create design",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
            is_completed=True,
        )
        task_create_frontend_architecture = Task.objects.create(
            name="Create frontend architecture",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
            is_completed=True,
        )
        task_create_backend_architecture = Task.objects.create(
            name="Create backend architecture",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_registration = Task.objects.create(
            name="Implement registration",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_authorization = Task.objects.create(
            name="Implement authorization",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_video_upload = Task.objects.create(
            name="Implement video upload",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_video_streaming = Task.objects.create(
            name="Implement video streaming",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_channel_creation = Task.objects.create(
            name="Implement channel creation",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_subscription = Task.objects.create(
            name="Implement subscription",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )
        task_implement_video_deleting = Task.objects.create(
            name="Implement video deleting",
            deadline=datetime(2024, 4, 30),
            priority="High",
            project=project,
        )

        task_create_db_structure.assignees.set((self.user,))
        task_create_design.assignees.set((self.user,))
        task_create_frontend_architecture.assignees.set((self.user,))
        task_create_backend_architecture.assignees.set((self.user,))
        task_implement_registration.assignees.set((self.user,))
        task_implement_authorization.assignees.set((self.user,))
        task_implement_video_upload.assignees.set((self.user,))
        task_implement_video_streaming.assignees.set((self.user,))
        task_implement_channel_creation.assignees.set((self.user,))
        task_implement_subscription.assignees.set((self.user,))
        task_implement_video_deleting.assignees.set((self.user,))

    def test_should_display_list_of_user_tasks(self) -> None:
        tasks = get_user_tasks(self.user)

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["page_obj"]), list(tasks)[:10])

    def test_should_display_list_of_tasks_with_pagination(self) -> None:
        tasks = get_user_tasks(self.user)

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["page_obj"]), list(tasks)[10:])

    def test_should_display_list_of_tasks_with_search(self) -> None:
        tasks = get_user_tasks(self.user, name="Create DB structure")

        res = self.client.get(self.url + "?task-name=Create DB structure")

        self.assertEqual(list(res.context["page_obj"]), list(tasks)[:1])

    def test_should_display_list_of_completed_tasks_if_is_completed_is_true(
        self,
    ) -> None:
        tasks = get_user_tasks(self.user, is_completed=True)

        res = self.client.get(self.url + "?is_completed=True")

        self.assertEqual(list(res.context["page_obj"]), list(tasks)[:10])

    def test_should_display_list_of_not_completed_tasks_if_is_completed_is_false(
        self,
    ) -> None:
        tasks = get_user_tasks(self.user, is_completed=False)

        res = self.client.get(self.url + "?is_completed=False")

        self.assertEqual(list(res.context["page_obj"]), list(tasks)[:10])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/my_tasks.html")
