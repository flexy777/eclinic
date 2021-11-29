# Generated by Django 3.2.7 on 2021-11-29 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eclinic_platform', '0006_auto_20211129_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]