# Generated by Django 2.1.2 on 2018-10-28 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AccountFrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Includes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('dispatchedDatetime', models.DateTimeField()),
                ('orderedDatetime', models.DateTimeField()),
                ('deliveredDatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Account')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Location')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='includes',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Order'),
        ),
        migrations.AddField(
            model_name='includes',
            name='supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Supply'),
        ),
        migrations.AddField(
            model_name='distance',
            name='distanceFrom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Location'),
        ),
        migrations.AddField(
            model_name='distance',
            name='distanceTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distanceTo', to='system.Location'),
        ),
        migrations.AddField(
            model_name='accountfrom',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Location'),
        ),
    ]