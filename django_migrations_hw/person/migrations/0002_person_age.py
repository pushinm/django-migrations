# Generated by Django 4.1.5 on 2023-01-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=18, verbose_name='age'),
        ),
    ]
