# Generated by Django 5.1.3 on 2024-11-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='username',
            field=models.CharField(default='default_user', max_length=1000),
        ),
    ]
