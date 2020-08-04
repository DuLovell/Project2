# Generated by Django 2.2 on 2020-08-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('desription', models.TextField(max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]