# Generated by Django 3.1.1 on 2020-12-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20201203_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('no_active', 'No Active')], max_length=10),
        ),
    ]
