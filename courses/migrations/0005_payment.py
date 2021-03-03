# Generated by Django 3.1.6 on 2021-02-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210220_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.CharField(max_length=50)),
                ('receipt_date', models.DateField()),
                ('amount', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('ch_no', models.IntegerField()),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('ch_date', models.DateField()),
            ],
        ),
    ]
