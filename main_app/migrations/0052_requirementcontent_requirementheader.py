# Generated by Django 3.0.5 on 2021-02-10 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0051_auto_20210202_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='requirementHeader',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=300)),
                ('subHeading', models.CharField(blank=True, max_length=700)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='requirementContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.requirementHeader')),
            ],
        ),
    ]