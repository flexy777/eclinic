# Generated by Django 3.2.7 on 2021-11-29 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eclinic_platform', '0011_alter_communication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='eclinic_platform.user'),
            preserve_default=False,
        ),
    ]