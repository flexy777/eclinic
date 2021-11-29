# Generated by Django 3.2.7 on 2021-11-29 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eclinic_platform', '0007_alter_review_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]