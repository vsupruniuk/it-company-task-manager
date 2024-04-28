from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Project, Tag


class PublicTagCreateTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:tag-create", kwargs={"pk": 1})

    def test_tag_create_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/projects/1/tags/create/", res.url)


class PrivateTagCreateTests(TestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(
            name="YouTube",
            description="Copy of YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=100_000_000,
        )

        self.url = reverse(
            "manager:tag-create",
            kwargs={"pk": self.project.pk},
        )

        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

    def test_should_be_possible_to_create_tag(self) -> None:
        name = "backend"
        form_data = {"name": name}

        self.client.post(self.url, data=form_data)

        created_tag = Tag.objects.get(name=name)

        self.assertEqual(created_tag.name, name)
        self.assertEqual(created_tag.project, self.project)

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/tag_form.html")
