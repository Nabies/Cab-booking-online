# Generated by Django 3.0.3 on 2020-09-10 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0004_auto_20200910_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
