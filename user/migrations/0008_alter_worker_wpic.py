# Generated by Django 3.2.4 on 2023-01-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_worker_wpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='wpic',
            field=models.ImageField(null=True, upload_to='static/worker'),
        ),
    ]
