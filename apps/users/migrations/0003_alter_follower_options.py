# Generated by Django 5.1.6 on 2025-02-27 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_follower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'ordering': ['-created_at']},
        ),
    ]
