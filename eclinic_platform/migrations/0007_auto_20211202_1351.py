# Generated by Django 3.2.7 on 2021-12-02 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eclinic_platform', '0006_alter_appointment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='appointment',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eclinic_platform.transactions'),
        ),
    ]
