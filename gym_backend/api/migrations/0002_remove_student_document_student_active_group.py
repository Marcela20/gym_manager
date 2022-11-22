# Generated by Django 4.1.3 on 2022-11-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='document',
        ),
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('instructor', models.CharField(max_length=50)),
                ('days', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=10)),
                ('limit', models.IntegerField(default=10)),
                ('level', models.IntegerField(default=1)),
                ('members', models.ManyToManyField(to='api.student')),
            ],
        ),
    ]
