# Generated by Django 4.1.6 on 2023-02-14 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_article_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='season',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]