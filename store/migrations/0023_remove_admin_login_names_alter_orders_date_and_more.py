# Generated by Django 4.2.6 on 2024-02-12 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_admin_login_names_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_login',
            name='names',
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 12, 16, 46, 23, 816214)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
