# Generated by Django 4.2.6 on 2023-11-10 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, default=5.04, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default='1-337-123-1234', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=200, max_digits=5, null=True),
        ),
    ]
