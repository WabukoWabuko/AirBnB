# Generated by Django 4.1.3 on 2024-12-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_emergency'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
