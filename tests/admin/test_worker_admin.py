from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.admin import WorkerAdmin
from manager.models import Team, Position


class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.user", password="Qwerty12345!"
        )

        self.site = AdminSite()

        self.client.force_login(self.admin_user)

        team = Team.objects.create(name="Avengers-developers")
        position = Position.objects.create(name="Developer", team=team)

        self.worker = get_user_model().objects.create(
            username="t.start",
            first_name="Tony",
            last_name="Stark",
            position=position,
            team=team,
        )

        self.worker_admin = WorkerAdmin(get_user_model(), self.site)

    def test_worker_position_listed(self) -> None:
        url = reverse("admin:manager_worker_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.worker.position)

    def test_worker_team_listed(self) -> None:
        url = reverse("admin:manager_worker_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.worker.team)

    def test_worker_detail_position_listed(self) -> None:
        url = reverse("admin:manager_worker_change", args=[self.worker.id])
        res = self.client.get(url)

        self.assertContains(res, self.worker.position)

    def test_worker_detail_team_listed(self) -> None:
        url = reverse("admin:manager_worker_change", args=[self.worker.id])
        res = self.client.get(url)

        self.assertContains(res, self.worker.team)

    def test_worker_create_first_name_listed(self) -> None:
        url = reverse("admin:manager_worker_add")
        res = self.client.get(url)

        self.assertContains(res, "id_first_name")

    def test_worker_create_last_name_listed(self) -> None:
        url = reverse("admin:manager_worker_add")
        res = self.client.get(url)

        self.assertContains(res, "id_last_name")

    def test_worker_create_email_listed(self) -> None:
        url = reverse("admin:manager_worker_add")
        res = self.client.get(url)

        self.assertContains(res, "id_email")

    def test_filtering_by_position(self) -> None:
        self.assertIn("position", self.worker_admin.list_filter)

    def test_filtering_by_team(self) -> None:
        self.assertIn("team", self.worker_admin.list_filter)
