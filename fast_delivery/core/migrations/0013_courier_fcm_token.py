# Generated by Django 4.2.13 on 2024-05-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_transaction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='fcm_token',
            field=models.TextField(blank=True),
        ),
    ]
