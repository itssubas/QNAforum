# Generated by Django 2.1.1 on 2018-10-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20181003_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]