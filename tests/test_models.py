from datetime import datetime

from django.test import TestCase

from manager.models import Position, TaskType, Tag, Worker, Task, Project, Team


class ModelTests(TestCase):
    def test_position_str(self) -> None:
        team = Team.objects.create(name="Avengers-developers")
        position = Position.objects.create(name="Software Engineer", team=team)

        self.assertEqual(str(position), f"Position: {position.name}")

    def test_task_type_str(self) -> None:
        project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=10_000_000,
        )
        task_type = TaskType.objects.create(name="Bugfix", project=project)

        self.assertEqual(str(task_type), f"Task type: {task_type.name}")

    def test_tag_str(self) -> None:
        project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=10_000_000,
        )
        tag = Tag.objects.create(name="bugfix", project=project)

        self.assertEqual(str(tag), f"Tag: {tag.name}")

    def test_worker_str(self) -> None:
        team = Team.objects.create(name="Avengers-developers")
        position = Position.objects.create(name="Software Engineer", team=team)
        worker = Worker.objects.create(
            username="t.stark",
            first_name="Tony",
            last_name="Stark",
            position=position,
        )

        self.assertEqual(
            str(worker),
            f"Worker: {worker.username} ({worker.first_name} {worker.last_name}), {worker.position.name}",
        )

    def test_task_str(self) -> None:
        task = Task(
            name="Fix user authorization issues",
            priority="high",
            deadline=datetime(2024, 1, 10),
        )

        date = task.deadline.strftime("%Y-%m-%d")

        self.assertEqual(
            str(task),
            f"Task: {task.name} (priority: {task.priority}, deadline: {date})",
        )

    def test_project_str(self) -> None:
        project = Project.objects.create(
            name="YouTube video hosting",
            start_date=datetime(2024, 1, 1),
            budget=10_000_000,
        )

        date = project.start_date.strftime("%Y-%m-%d")

        self.assertEqual(
            str(project),
            f"Project: {project.name} (budget: {project.budget}, start date: {date})",
        )

    def test_team_str(self) -> None:
        team = Team.objects.create(name="Avengers-developers")

        self.assertEqual(str(team), f"Team: {team.name}")
