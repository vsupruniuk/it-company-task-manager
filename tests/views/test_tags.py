from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Tag
from manager.services import get_project_tags


class PublicTagsViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:tag-list", kwargs={"pk": 1})

    def test_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/projects/1/tags/")


class PrivateTagsViewTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.url = reverse("manager:tag-list", kwargs={"pk": self.project.pk})

        Tag.objects.create(name="backend", project=self.project)
        Tag.objects.create(name="frontend", project=self.project)
        Tag.objects.create(name="database", project=self.project)
        Tag.objects.create(name="security", project=self.project)
        Tag.objects.create(name="testing", project=self.project)
        Tag.objects.create(name="deployment", project=self.project)
        Tag.objects.create(name="analytics", project=self.project)
        Tag.objects.create(name="design", project=self.project)
        Tag.objects.create(name="documentation", project=self.project)
        Tag.objects.create(name="integration", project=self.project)
        Tag.objects.create(name="performance", project=self.project)

    def test_should_display_list_of_tags(self) -> None:
        tags = get_project_tags(self.project.id)

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["tag_list"]), list(tags)[:10])

    def test_should_display_list_of_tags_with_pagination(self) -> None:
        tags = get_project_tags(self.project.id)

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["tag_list"]), list(tags)[10:])

    def test_should_display_list_of_tags_with_search(self) -> None:
        tags = get_project_tags(self.project.id, tag_name="backend")

        res = self.client.get(self.url + "?tag-name=backend")

        self.assertEqual(list(res.context["tag_list"]), list(tags)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/tag_list.html")
