# Generated by Django 3.2 on 2022-05-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_gettutor_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gettutor',
            name='duration',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
