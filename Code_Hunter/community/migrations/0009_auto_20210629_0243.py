# Generated by Django 3.2.3 on 2021-06-28 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_auto_20210629_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitycomment',
            name='author',
            field=models.CharField(default='익명', max_length=20),
        ),
        migrations.AlterField(
            model_name='communitycomment',
            name='origin_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='community.community'),
        ),
    ]