# Generated by Django 3.2.4 on 2023-01-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='wpic',
            field=models.ImageField(null=True, upload_to='static/worker'),
        ),
    ]
