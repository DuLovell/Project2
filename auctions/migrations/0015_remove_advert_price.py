# Generated by Django 2.2 on 2020-08-03 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20200803_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='price',
        ),
    ]
