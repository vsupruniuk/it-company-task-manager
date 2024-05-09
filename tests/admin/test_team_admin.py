from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import TeamAdmin
from manager.admin_filers import ProjectListFilter
from manager.models import Team


class ProjectTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        team_lead = get_user_model().objects.create(
            username="t.stark", first_name="Tony", last_name="Stark"
        )

        self.team = Team.objects.create(name="Avengers-developers", team_lead=team_lead)

        self.team_admin = TeamAdmin(Team, self.site)

    def test_team_name_listed(self) -> None:
        url = reverse("admin:manager_team_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.team.name)

    def test_team_team_lead_listed(self) -> None:
        url = reverse("admin:manager_team_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.team.team_lead)

    def test_search_by_name(self) -> None:
        self.assertIn("name", self.team_admin.search_fields)

    def test_filtering_by_team_lead(self) -> None:
        self.assertIn("team_lead", self.team_admin.list_filter)

    def test_filtering_by_project(self) -> None:
        self.assertIn(ProjectListFilter, self.team_admin.list_filter)
