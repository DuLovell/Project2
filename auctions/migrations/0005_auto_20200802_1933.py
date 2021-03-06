# Generated by Django 2.2 on 2020-08-02 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_advert_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='user',
            field=models.CharField(default='admin', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advert',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Bid'),
        ),
    ]
