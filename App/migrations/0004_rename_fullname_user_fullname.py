# Generated by Django 4.2.16 on 2024-12-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_user_userverification_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fullname',
            new_name='fullName',
        ),
    ]
