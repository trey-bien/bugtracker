# Generated by Django 3.1 on 2020-08-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugapp', '0002_auto_20200828_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('N', 'New'), ('C', 'Complete'), ('P', 'In Progress'), ('I', 'Invalid')], default='N', max_length=20),
        ),
    ]
