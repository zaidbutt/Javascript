# Generated by Django 3.1.7 on 2021-06-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='end_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
