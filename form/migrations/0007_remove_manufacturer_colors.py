# Generated by Django 3.1 on 2020-08-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20200828_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='colors',
        ),
    ]