# Generated by Django 4.1 on 2022-09-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_ability_options_alter_education_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexprience',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
    ]
