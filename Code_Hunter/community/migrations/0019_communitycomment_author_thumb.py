# Generated by Django 3.2.3 on 2021-07-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_alter_community_pub_dateonly'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitycomment',
            name='author_thumb',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]