# Generated by Django 3.2.5 on 2021-07-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
