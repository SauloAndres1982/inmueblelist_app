# Generated by Django 4.1.7 on 2023-04-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inmuebleslist_app", "0002_empresa_inmueble_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inmueble",
            name="created",
        ),
    ]
