# Generated by Django 4.0.2 on 2022-03-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
