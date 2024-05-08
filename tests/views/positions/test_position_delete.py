from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position


class PublicPositionDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:position-delete", kwargs={"pk": 1})

    def test_position_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/positions/1/delete/", res.url)


class PrivatePositionDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team = Team.objects.create(name="Avengers")
        self.position = Position.objects.create(name="Developer", team=self.team)

        self.url = reverse(
            "manager:position-delete",
            kwargs={"pk": self.position.pk},
        )

    def test_should_delete_position(self) -> None:
        self.client.post(self.url)

        position = Position.objects.filter(name="Developer")

        self.assertEqual(list(position), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/position_confirm_delete.html")
