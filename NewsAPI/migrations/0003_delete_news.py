# Generated by Django 3.2.5 on 2021-07-28 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsAPI', '0002_alter_news_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]
