# Generated by Django 3.2.3 on 2021-07-15 18:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wanted', '0023_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='applicants',
            field=models.ManyToManyField(blank=True, null=True, related_name='applying', to=settings.AUTH_USER_MODEL),
        ),
    ]