# Generated by Django 3.1.6 on 2021-02-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20210227_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='remarks',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10),
        ),
    ]