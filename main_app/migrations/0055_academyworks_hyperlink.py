# Generated by Django 3.0.5 on 2021-03-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0054_advantagescontent_advantagesheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='academyworks',
            name='hyperlink',
            field=models.TextField(blank=True),
        ),
    ]
