# Generated by Django 4.1.3 on 2022-11-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('startDate', models.CharField(default='', max_length=40)),
                ('endDate', models.CharField(default='', max_length=40)),
                ('rRule', models.CharField(default='', max_length=40)),
            ],
        ),
    ]