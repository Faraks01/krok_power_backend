# Generated by Django 3.1 on 2020-08-28 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0013_auto_20200828_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackform',
            old_name='manufacturers',
            new_name='manufacturer',
        ),
    ]
