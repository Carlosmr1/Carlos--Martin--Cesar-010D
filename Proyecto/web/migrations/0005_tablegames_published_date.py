# Generated by Django 4.1.9 on 2023-06-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_videogames_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablegames',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
