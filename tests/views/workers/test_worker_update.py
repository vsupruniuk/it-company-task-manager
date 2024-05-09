from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position


class PublicWorkerUpdateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-update", kwargs={"pk": 1})

    def test_worker_update_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/workers/1/update/", res.url)


class PrivateWorkerUpdateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team = Team.objects.create(name="Avengers-developers")
        self.position = Position.objects.create(name="Developer", team=self.team)
        self.worker = get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            team=self.team,
            position=self.position,
            password="Qwerty12345!",
        )

        self.new_team = Team.objects.create(name="Avengers-designers")
        self.new_position = Position.objects.create(name="Designer", team=self.new_team)

        self.url = reverse("manager:worker-update", kwargs={"pk": self.worker.pk})

    def test_should_update_worker(self) -> None:
        form_data = {
            "first_name": "Steve",
            "last_name": "Rogers",
            "username": "s.rogers",
            "team": self.new_team.id,
            "position": self.position.id,
            "password1": "Qwerty12345!",
            "password2": "Qwerty12345!",
        }

        self.client.post(self.url, data=form_data)

        updated_worker = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(updated_worker.first_name, form_data.get("first_name"))
        self.assertEqual(updated_worker.last_name, form_data.get("last_name"))
        self.assertEqual(updated_worker.username, form_data.get("username"))
        self.assertEqual(updated_worker.team.id, form_data.get("team"))
        self.assertEqual(updated_worker.position.id, form_data.get("position"))

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/worker_form.html")
