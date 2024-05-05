from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position


class PublicPositionDetailTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:position-detail", kwargs={"pk": 1, "id": 1})

    def test_position_detail_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/1/positions/1/", res.url)


class PrivatePositionDetailTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers")
        self.position = Position.objects.create(name="Developer", team=self.team)

        self.url = reverse(
            "manager:position-detail",
            kwargs={"pk": self.team.pk, "id": self.position.id},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_display_position_details(self) -> None:
        res = self.client.get(self.url)

        self.assertContains(res, self.position.name)
        self.assertContains(res, self.position.team.name)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/position_detail.html")
