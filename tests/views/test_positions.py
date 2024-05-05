from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Team, Position
from manager.services import get_team_positions


class PublicPositionViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:position-list", kwargs={"pk": 1})

    def test_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/teams/1/positions/")


class PrivateTagsViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.team = Team.objects.create(name="Avengers")

        self.url = reverse("manager:position-list", kwargs={"pk": self.team.pk})

        Position.objects.create(name="Developer", team=self.team)
        Position.objects.create(name="Project Manager", team=self.team)
        Position.objects.create(name="Software Engineer", team=self.team)
        Position.objects.create(name="Quality Assurance Analyst", team=self.team)
        Position.objects.create(name="UI/UX Designer", team=self.team)
        Position.objects.create(name="Data Scientist", team=self.team)
        Position.objects.create(name="Systems Analyst", team=self.team)
        Position.objects.create(name="Database Administrator", team=self.team)
        Position.objects.create(name="Network Engineer", team=self.team)
        Position.objects.create(name="DevOps Engineer", team=self.team)
        Position.objects.create(name="Technical Writer", team=self.team)

    def test_should_display_list_of_positions(self) -> None:
        positions = get_team_positions(self.team.id)

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["position_list"]), list(positions)[:10])

    def test_should_display_list_of_positions_with_pagination(self) -> None:
        positions = get_team_positions(self.team.id)

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["position_list"]), list(positions)[10:])

    def test_should_display_list_of_positions_with_search(self) -> None:
        positions = get_team_positions(self.team.id, position_name="developer")

        res = self.client.get(self.url + "?position-name=developer")

        self.assertEqual(list(res.context["position_list"]), list(positions)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/position_list.html")
