# Generated by Django 2.1.2 on 2018-11-05 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dispatcher', '0007_auto_20181101_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatcherAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PackerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='AccountFrom',
            new_name='HAAccount',
        ),
        migrations.RemoveField(
            model_name='account',
            name='position',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Queued for Processing', 'Queued for Processing'), (' Processing by Warehouse', ' Processing by Warehouse'), ('Queued for Dispatched', 'Queued for Dispatched'), ('Dispatched', 'Dispatched'), ('Delivered', 'Delivered')], default='Queued for Processing', max_length=30),
        ),
        migrations.AddField(
            model_name='packeraccount',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Account'),
        ),
        migrations.AddField(
            model_name='packeraccount',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Location'),
        ),
        migrations.AddField(
            model_name='dispatcheraccount',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Account'),
        ),
        migrations.AddField(
            model_name='dispatcheraccount',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Location'),
        ),
    ]