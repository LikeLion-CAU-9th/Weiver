# Generated by Django 3.2.3 on 2021-07-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanted', '0017_auto_20210703_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='author',
            field=models.CharField(default='코딩뉴비', max_length=8, verbose_name='닉네임'),
        ),
    ]