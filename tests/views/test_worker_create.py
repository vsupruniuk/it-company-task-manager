from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position


class PublicWorkerCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-create")

    def test_worker_create_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/workers/create/", res.url)


class PrivateWorkerCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-create")

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team = Team.objects.create(name="Avengers-developers")
        self.position = Position.objects.create(name="Developer", team=self.team)

    def test_should_create_worker_from_user_data(self) -> None:
        form_data = {
            "username": "t.stark",
            "first_name": "Tony",
            "last_name": "Stark",
            "team": self.team.id,
            "position": self.position.id,
            "password1": "Qwerty12345!",
            "password2": "Qwerty12345!",
        }

        self.client.post(self.url, data=form_data)

        created_worker = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(created_worker.username, form_data.get("username"))
        self.assertEqual(created_worker.first_name, form_data.get("first_name"))
        self.assertEqual(created_worker.last_name, form_data.get("last_name"))
        self.assertEqual(created_worker.team.id, form_data.get("team"))
        self.assertEqual(created_worker.position.id, form_data.get("position"))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/worker_form.html")
