# Generated by Django 3.1 on 2020-08-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('New', 'New'), ('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Invalid', 'Invalid')], default='New', max_length=20),
        ),
    ]
