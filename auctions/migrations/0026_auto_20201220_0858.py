# Generated by Django 3.1.1 on 2020-12-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_auto_20201219_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='bids',
            name='bid',
        ),
        migrations.AddField(
            model_name='bids',
            name='bid',
            field=models.ManyToManyField(to='auctions.bid'),
        ),
    ]
