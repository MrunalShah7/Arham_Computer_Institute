# Generated by Django 3.1.6 on 2021-02-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_addmission_time_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='ch_date',
            new_name='payment_date',
        ),
        migrations.AlterField(
            model_name='payment',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='branch_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='ch_no',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Check', 'Check'), ('Card', 'Card')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
