# Generated by Django 3.2.7 on 2021-11-30 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eclinic_platform', '0003_auto_20211130_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_specialist', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]