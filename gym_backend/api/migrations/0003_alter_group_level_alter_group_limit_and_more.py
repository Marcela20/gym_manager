# Generated by Django 4.1.3 on 2022-11-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='level',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='limit',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(null=True, related_name='members', to='api.student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='time',
            field=models.ManyToManyField(null=True, related_name='events', to='api.event'),
        ),
    ]
