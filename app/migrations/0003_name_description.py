# Generated by Django 5.0.7 on 2024-08-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_name_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='description',
            field=models.TextField(default='No description'),
        ),
    ]
