# Generated by Django 3.1.7 on 2021-05-16 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210517_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bider',
        ),
    ]
