# Generated by Django 4.2.1 on 2023-06-09 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_article_user_readinglist_article_readinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readinglist',
            name='category',
            field=models.CharField(choices=[('sports', 'Sports'), ('science', 'Science'), ('technology', 'Technology'), ('entertainment', 'Entertainment')], default='sports', max_length=100),
        ),
    ]