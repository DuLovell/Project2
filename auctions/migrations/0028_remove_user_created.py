# Generated by Django 2.2 on 2020-08-05 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_user_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
    ]
