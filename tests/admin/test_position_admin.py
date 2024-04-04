from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import PositionAdmin
from manager.admin_filers import TeamListFilter
from manager.models import Position, Team


class PositionTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        team = Team.objects.create(name="Avengers-developers")
        self.position = Position.objects.create(name="Developer", team=team)

        self.position_admin = PositionAdmin(Position, self.site)

    def test_position_name_listed(self) -> None:
        url = reverse("admin:manager_position_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.position.name)

    def test_position_team_listed(self) -> None:
        url = reverse("admin:manager_position_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.position.team)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.position_admin.search_fields)

    def test_filtering_by_team(self) -> None:
        self.assertIn(TeamListFilter, self.position_admin.list_filter)
