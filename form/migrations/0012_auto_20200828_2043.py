# Generated by Django 3.1 on 2020-08-28 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0011_auto_20200828_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackform',
            old_name='rosette_manufacturer',
            new_name='manufacturer',
        ),
    ]
