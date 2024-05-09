from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position


class PublicPositionCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:position-create", kwargs={"pk": 1})

    def test_position_create_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/1/positions/create/", res.url)


class PrivatePositionCreateTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers")

        self.url = reverse(
            "manager:position-create",
            kwargs={"pk": self.team.pk},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_be_possible_to_create_position(self) -> None:
        name = "Developer"
        form_data = {"name": name}

        self.client.post(self.url, data=form_data)

        created_position = Position.objects.get(name=name)

        self.assertEqual(created_position.name, name)
        self.assertEqual(created_position.team, self.team)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/position_form.html")
