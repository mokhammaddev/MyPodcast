# Generated by Django 4.1.6 on 2023-02-14 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_article_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.season'),
        ),
    ]
