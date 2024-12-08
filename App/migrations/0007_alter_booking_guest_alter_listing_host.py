# Generated by Django 4.1.3 on 2024-12-08 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0006_alter_listing_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='App.user'),
        ),
    ]
