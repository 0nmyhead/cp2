# Generated by Django 4.1 on 2022-11-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(default="", max_length=100, unique=True)),
                ("username", models.CharField(default="", max_length=100, unique=True)),
                (
                    "phone",
                    models.CharField(blank=True, default="", max_length=30, null=True),
                ),
                ("age", models.IntegerField(blank=True, default="", null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
