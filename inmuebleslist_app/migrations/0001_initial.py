# Generated by Django 4.1.7 on 2023-04-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inmueble",
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
                ("direccion", models.CharField(max_length=250)),
                ("pais", models.CharField(max_length=150)),
                ("descripcion", models.CharField(max_length=500)),
                ("imagen", models.CharField(max_length=900)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]