# Generated by Django 3.1.6 on 2021-02-20 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210220_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addmission', to='courses.courses_master')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addmission', to='courses.student')),
            ],
        ),
    ]
