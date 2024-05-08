from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Tag


class PublicTagDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:tag-delete", kwargs={"pk": 1})

    def test_tag_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/tags/1/delete/", res.url)


class PrivateTagDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.project = Project.objects.create(
            name="YouTube",
            description="YouTube video hosting",
            start_date=date(2024, 1, 1),
            budget=100_000_000,
        )
        self.tag = Tag.objects.create(name="backend", project=self.project)

        self.url = reverse(
            "manager:tag-delete",
            kwargs={"pk": self.tag.pk},
        )

    def test_should_delete_tag(self) -> None:
        self.client.post(self.url)

        tag = Project.objects.filter(name="backend")

        self.assertEqual(list(tag), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/tag_confirm_delete.html")
