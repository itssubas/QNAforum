# Generated by Django 2.1.1 on 2018-10-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='portfolio',
            field=models.URLField(blank=True),
        ),
    ]
