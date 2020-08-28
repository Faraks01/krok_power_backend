# Generated by Django 3.1 on 2020-08-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20200826_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Цвет корпуса',
                'verbose_name_plural': 'Цвета корпуса',
            },
        ),
        migrations.CreateModel(
            name='RosetteColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Цвет розеток',
                'verbose_name_plural': 'Цвета розеток',
            },
        ),
    ]
