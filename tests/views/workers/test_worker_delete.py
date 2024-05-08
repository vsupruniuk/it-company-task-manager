from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PublicWorkerDeleteTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-delete", kwargs={"pk": 1})

    def test_worker_delete_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual("/accounts/login/?next=/workers/1/delete/", res.url)


class PrivateWorkerDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        self.worker = get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )

        self.url = reverse("manager:worker-delete", kwargs={"pk": self.worker.pk})

    def test_should_delete_worker(self) -> None:
        self.client.post(self.url)

        project = get_user_model().objects.filter(username="t.stark")

        self.assertEqual(list(project), [])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/worker_confirm_delete.html")
