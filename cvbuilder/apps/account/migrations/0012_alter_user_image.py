# Generated by Django 4.1 on 2022-09-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
