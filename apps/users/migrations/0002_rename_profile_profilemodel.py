# Generated by Django 5.0.7 on 2024-08-02 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileModel',
        ),
    ]