# Generated by Django 4.1.6 on 2023-02-14 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_season_article_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.season'),
            preserve_default=False,
        ),
    ]
