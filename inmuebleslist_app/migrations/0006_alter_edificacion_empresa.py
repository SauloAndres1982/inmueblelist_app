# Generated by Django 4.1.7 on 2023-04-04 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inmuebleslist_app", "0005_edificacion_empresa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="edificacion",
            name="empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="edificacionlist",
                to="inmuebleslist_app.empresa",
            ),
        ),
    ]
