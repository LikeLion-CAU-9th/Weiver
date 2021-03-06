# Generated by Django 3.2.3 on 2021-06-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanted', '0004_auto_20210610_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quest',
            name='status',
            field=models.CharField(choices=[('UNSOLVED', 'UNSOLVED'), ('SOLVING', 'SOLVING'), ('SOLVED', 'SOLVED')], default='UNSOLVED', max_length=10),
        ),
        migrations.AddField(
            model_name='quest',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quest',
            name='author',
            field=models.CharField(default='익명', max_length=8, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='bounty',
            field=models.IntegerField(default=0, verbose_name='현상금'),
        ),
    ]
