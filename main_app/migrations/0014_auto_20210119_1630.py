# Generated by Django 3.0.5 on 2021-01-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_newsandupdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandupdates',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]