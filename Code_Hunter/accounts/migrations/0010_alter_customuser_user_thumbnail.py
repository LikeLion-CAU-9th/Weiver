# Generated by Django 3.2.3 on 2021-07-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customuser_user_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_thumbnail',
            field=models.ImageField(blank=True, default='./user_thumbnails/default-user.png', null=True, upload_to='user_thumbnails'),
        ),
    ]
