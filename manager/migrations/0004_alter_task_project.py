# Generated by Django 5.0.3 on 2024-04-07 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0003_alter_task_assignees_alter_task_reporter_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="manager.project",
            ),
        ),
    ]