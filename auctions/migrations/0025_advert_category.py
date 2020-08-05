# Generated by Django 2.2 on 2020-08-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20200804_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('toys', 'Toys'), ('electronics', 'Electronics'), ('home', 'Home'), ('appliances', 'Appliances'), ('books', 'Books')], default=None, max_length=32),
            preserve_default=False,
        ),
    ]
