# Generated by Django 4.2.16 on 2024-12-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_address',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='fullname',
        ),
    ]
