# Generated by Django 3.2 on 2022-05-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220522_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gettutor',
            name='address',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='bustop',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='classofkid',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='curiculum',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='fullname',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='modeoftutor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='state',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='gettutor',
            name='typeoftutor',
            field=models.CharField(max_length=100),
        ),
    ]
