# Generated by Django 2.1.3 on 2018-12-01 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASP_webApp', '0013_auto_20181201_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='priority',
            field=models.CharField(choices=[('High', '1'), ('Medium', '2'), ('Low', '3')], default=3, max_length=10),
        ),
    ]