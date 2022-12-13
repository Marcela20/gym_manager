# Generated by Django 4.1.3 on 2022-12-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_subgroup_hour"),
    ]

    operations = [
        migrations.AddField(
            model_name="date",
            name="subgroups",
            field=models.ManyToManyField(
                blank=True, related_name="subgroups_dates", to="api.subgroup"
            ),
        ),
    ]