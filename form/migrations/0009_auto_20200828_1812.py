# Generated by Django 3.1 on 2020-08-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_wirelength'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wirelength',
            options={'ordering': ('name',), 'verbose_name': 'Длинна кабеля', 'verbose_name_plural': 'Длинна кабелей'},
        ),
        migrations.RemoveField(
            model_name='wirelength',
            name='length',
        ),
        migrations.AddField(
            model_name='wirelength',
            name='name',
            field=models.FloatField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
