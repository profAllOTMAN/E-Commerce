# Generated by Django 3.1.1 on 2020-12-03 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201202_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='categoryname',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='list_category',
            new_name='listcategory',
        ),
    ]
