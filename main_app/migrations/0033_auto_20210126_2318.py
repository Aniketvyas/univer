# Generated by Django 3.0.5 on 2021-01-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_accreditatedcenters_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accreditatedcenters',
            name='flag',
            field=models.FileField(upload_to=''),
        ),
    ]
