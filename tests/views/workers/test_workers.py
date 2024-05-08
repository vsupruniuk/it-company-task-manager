from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.services import get_workers


class PublicWorkersViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-list")

    def test_workers_login_required(self) -> None:
        res = self.client.get(self.url)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, "/accounts/login/?next=/workers/")


class PrivateWorkersViewTests(TestCase):
    def setUp(self) -> None:
        self.url = reverse("manager:worker-list")
        self.user = get_user_model().objects.create_user(
            first_name="Admin",
            last_name="User",
            username="admin",
            password="Qwerty12345!",
        )

        self.client.force_login(self.user)

        get_user_model().objects.create_user(
            first_name="Tony",
            last_name="Stark",
            username="t.stark",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Steve",
            last_name="Rogers",
            username="s.rogers",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Natasha",
            last_name="Romanoff",
            username="n.romanoff",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Bruce",
            last_name="Banner",
            username="b.banner",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Thor",
            last_name="Odinson",
            username="t.odinson",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Peter",
            last_name="Parker",
            username="p.parker",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Wanda",
            last_name="Maximoff",
            username="w.maximoff",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Clint",
            last_name="Barton",
            username="c.barton",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="James",
            last_name="Rhodes",
            username="j.rhodes",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Stephen",
            last_name="Strange",
            username="s.strange",
            password="Qwerty12345!",
        )
        get_user_model().objects.create_user(
            first_name="Carol",
            last_name="Danvers",
            username="c.danvers",
            password="Qwerty12345!",
        )

    def test_should_display_list_of_workers(self) -> None:
        workers = get_workers()

        res = self.client.get(self.url)

        self.assertEqual(list(res.context["worker_list"]), list(workers)[:10])

    def test_should_display_list_of_workers_with_pagination(self) -> None:
        workers = get_workers()

        res = self.client.get(self.url + "?page=2")

        self.assertEqual(list(res.context["worker_list"]), list(workers)[10:])

    def test_should_display_list_of_workers_with_search(self) -> None:
        workers = get_workers(username="stark")

        res = self.client.get(self.url + "?username=stark")

        self.assertEqual(list(res.context["worker_list"]), list(workers)[:1])

    def test_should_use_proper_template(self) -> None:
        res = self.client.get(self.url)

        self.assertTemplateUsed(res, "manager/worker_list.html")
