# Generated by Django 3.1.7 on 2021-04-30 03:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_listing_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
