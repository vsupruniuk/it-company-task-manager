from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Position, Team


class PublicWorkerDetailTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-detail", kwargs={"pk": 1})

    def test_worker_detail_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/workers/1/", res.url)


class PrivateWorkerDetailTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers-developers")
        self.position = Position.objects.create(name="Developer", team=self.team)

        self.worker = get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
            position=self.position,
            team=self.team,
        )
        self.url = reverse("manager:worker-detail", kwargs={"pk": self.worker.pk})

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_display_worker_details(self) -> None:
        res = self.client.get(self.url)

        self.assertContains(res, self.worker.username)
        self.assertContains(res, self.worker.first_name)
        self.assertContains(res, self.worker.last_name)
        self.assertContains(res, self.worker.email)
        self.assertContains(res, self.worker.position.name)
        self.assertContains(res, self.worker.team.name)
        self.assertContains(res, self.worker.last_login)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/worker_detail.html")
