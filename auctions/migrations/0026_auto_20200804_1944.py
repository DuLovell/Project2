# Generated by Django 2.2 on 2020-08-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_advert_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home'), ('Appliances', 'Appliances'), ('Books', 'Books')], max_length=32),
        ),
    ]
