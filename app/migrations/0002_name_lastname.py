# Generated by Django 5.0.7 on 2024-08-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='lastname',
            field=models.CharField(default='Doe', max_length=100),
        ),
    ]
