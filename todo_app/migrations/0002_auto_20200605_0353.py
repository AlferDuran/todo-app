# Generated by Django 3.0.7 on 2020-06-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
