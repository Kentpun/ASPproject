# Generated by Django 2.1.3 on 2018-11-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ASP_webApp', '0006_auto_20181120_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='firstname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='lastname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
