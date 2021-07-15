# Generated by Django 3.2.3 on 2021-07-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customuser_user_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='average_time',
            field=models.CharField(default='0D 0H', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='career',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='stack',
            field=models.TextField(default=''),
        ),
    ]
