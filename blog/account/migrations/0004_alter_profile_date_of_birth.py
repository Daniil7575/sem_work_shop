# Generated by Django 4.1 on 2022-08-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_date_of_birt_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
