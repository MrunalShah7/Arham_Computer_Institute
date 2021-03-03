# Generated by Django 3.1.6 on 2021-02-25 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_addmission_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmission',
            name='payment',
        ),
        migrations.AddField(
            model_name='payment',
            name='admission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='adm', to='courses.addmission'),
        ),
    ]
