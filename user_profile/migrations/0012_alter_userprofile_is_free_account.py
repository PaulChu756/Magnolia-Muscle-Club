# Generated by Django 4.2.6 on 2023-12-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_free_account',
            field=models.BooleanField(default=False),
        ),
    ]