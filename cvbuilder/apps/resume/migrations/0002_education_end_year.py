# Generated by Django 4.1 on 2022-09-16 08:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='end_year',
            field=models.PositiveIntegerField(default=1390, validators=[django.core.validators.MinValueValidator(1380), django.core.validators.MaxValueValidator(1401)]),
            preserve_default=False,
        ),
    ]
