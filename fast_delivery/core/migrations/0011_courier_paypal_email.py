# Generated by Django 4.2.13 on 2024-05-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_courier_job_courier'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
