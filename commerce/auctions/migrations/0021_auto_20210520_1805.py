# Generated by Django 3.1.7 on 2021-05-20 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20210517_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auctions.bid'),
        ),
    ]
