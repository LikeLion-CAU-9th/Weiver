# Generated by Django 3.2.3 on 2021-07-14 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0028_alter_community_pub_dateonly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='pub_dateonly',
            field=models.DateField(default=datetime.date.today),
        ),
    ]