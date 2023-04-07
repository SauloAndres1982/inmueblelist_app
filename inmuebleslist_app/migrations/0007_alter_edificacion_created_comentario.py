# Generated by Django 4.1.7 on 2023-04-04 22:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inmuebleslist_app", "0006_alter_edificacion_empresa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="edificacion",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name="Comentario",
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
                (
                    "calificacion",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("texto", models.CharField(max_length=200, null=True)),
                ("acive", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                (
                    "edificacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to="inmuebleslist_app.edificacion",
                    ),
                ),
            ],
        ),
    ]