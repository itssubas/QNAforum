# Generated by Django 2.1.1 on 2018-10-05 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='tag', to='Qna.Questions'),
        ),
    ]