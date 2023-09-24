# Generated by Django 4.2.5 on 2023-09-19 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.CharField(max_length=15, verbose_name="Государственный номер")),
                ("brand", models.CharField(max_length=20, verbose_name="Марка")),
                ("model", models.CharField(max_length=20, verbose_name="Модель")),
                ("color", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "автомобиль",
                "verbose_name_plural": "автомобили",
                "db_table": "car",
            },
        ),
        migrations.CreateModel(
            name="CarOwner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("last_name", models.CharField(max_length=30, verbose_name="Фамилия")),
                ("first_name", models.CharField(max_length=30, verbose_name="Имя")),
                ("birth_date", models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")),
            ],
            options={
                "verbose_name": "автовладелец",
                "verbose_name_plural": "автовладельцы",
                "db_table": "car_owner",
            },
        ),
        migrations.CreateModel(
            name="Ownership",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start_date", models.DateTimeField(verbose_name="Дата начала")),
                ("end_date", models.DateTimeField(blank=True, null=True, verbose_name="Дата начала")),
                (
                    "car",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ownerships",
                        to="project_first_app.car",
                        verbose_name="Автомобиль",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ownerships",
                        to="project_first_app.carowner",
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "владение",
                "verbose_name_plural": "владения",
                "db_table": "ownership",
            },
        ),
        migrations.CreateModel(
            name="DrivingLicence",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.CharField(max_length=10, verbose_name="Номер удостоверения")),
                ("type", models.CharField(max_length=10, verbose_name="Тип")),
                ("issue_date", models.DateTimeField(verbose_name="Дата выдачи")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="licences",
                        to="project_first_app.carowner",
                        verbose_name="Владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "водительское удостоверение",
                "verbose_name_plural": "водительские удостоверения",
                "db_table": "driving_licence",
            },
        ),
    ]