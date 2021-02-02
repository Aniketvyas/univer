# Generated by Django 3.0.5 on 2021-01-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20210119_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactQuery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contactNumber', models.BigIntegerField()),
                ('country', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('createDate', models.DateTimeField()),
            ],
        ),
    ]