# Generated by Django 4.1 on 2022-09-21 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyWatchList',
            new_name='MyWatchListItem',
        ),
    ]
