# Generated by Django 2.1.2 on 2018-10-28 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dispatcher', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Includes',
            new_name='Include',
        ),
    ]