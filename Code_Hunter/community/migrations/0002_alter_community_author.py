# Generated by Django 3.2.3 on 2021-06-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='author',
            field=models.CharField(default='익명', max_length=20, verbose_name='작성자'),
        ),
    ]