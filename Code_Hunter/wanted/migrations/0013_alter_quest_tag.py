# Generated by Django 3.2.3 on 2021-06-27 11:14

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wanted', '0012_alter_quest_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='tag',
        ),
        migrations.AddField(
            model_name='quest',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
