# Generated by Django 3.1 on 2020-08-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
    ]
