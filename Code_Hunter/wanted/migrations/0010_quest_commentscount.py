# Generated by Django 3.2.3 on 2021-06-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanted', '0009_alter_quest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='commentscount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]