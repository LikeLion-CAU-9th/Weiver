# Generated by Django 3.2.3 on 2021-07-01 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_community_pub_dateonly'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='today_or_not',
        ),
    ]
