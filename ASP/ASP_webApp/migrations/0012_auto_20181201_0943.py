# Generated by Django 2.1.3 on 2018-12-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASP_webApp', '0011_auto_20181201_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='priority',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3)], default=3, max_length=10),
        ),
    ]
