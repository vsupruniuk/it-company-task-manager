from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position


class PublicPositionUpdateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:position-update", kwargs={"pk": 1, "id": 1})

    def test_tag_update_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/teams/1/positions/1/update/", res.url)


class PrivatePositionUpdateTests(TestCase):
    def setUp(self) -> None:
        self.team = Team.objects.create(name="Avengers")
        self.position = Position.objects.create(name="Developer", team=self.team)

        self.url = reverse(
            "manager:position-update",
            kwargs={"pk": self.team.pk, "id": self.position.id},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_be_possible_to_update_position(self) -> None:
        name = "Designer"
        form_data = {"name": name}

        self.client.post(self.url, data=form_data)

        updated_position = Position.objects.get(name=name)

        self.assertEqual(updated_position.name, name)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/position_form.html")
