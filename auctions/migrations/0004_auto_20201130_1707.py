# Generated by Django 3.1.1 on 2020-11-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201129_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='categorys',
            field=models.IntegerField(),
        ),
    ]
