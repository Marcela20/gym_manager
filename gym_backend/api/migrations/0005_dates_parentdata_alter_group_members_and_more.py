# Generated by Django 4.1.3 on 2022-11-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_dates_group_dates_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='dates',
            name='parentData',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='members', to='api.student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='time',
            field=models.ManyToManyField(related_name='events', to='api.event'),
        ),
    ]
