# Generated by Django 4.2.3 on 2023-09-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplement_store', '0013_alter_support_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]