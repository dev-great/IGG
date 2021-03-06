# Generated by Django 3.2 on 2022-05-21 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial', '0003_auto_20220402_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Becometutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=15)),
                ('whatsappnumber', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=500)),
                ('primarylanguage', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('subjects', models.CharField(max_length=5000)),
                ('teachinglocations', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenceCode', models.CharField(blank=True, default='', max_length=100)),
                ('paystackAccessCode', models.CharField(blank=True, default='', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('duration', models.PositiveBigIntegerField(default=30)),
                ('paymentFor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tutorial.tutormodel')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('start', models.CharField(max_length=300)),
                ('stop', models.CharField(max_length=300)),
                ('roll', models.CharField(max_length=300)),
                ('active', models.BooleanField()),
                ('tutor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.becometutor')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires_in', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('subscriber', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='account.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(blank=True, default=False, max_length=20, null=True)),
                ('fullname', models.CharField(blank=True, default=False, max_length=500, null=True)),
                ('address', models.TextField(blank=True, default=False, max_length=5000, null=True)),
                ('profilepix', models.FileField(blank=True, default=0, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gettutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kidsnum', models.CharField(max_length=50)),
                ('classofkid', models.CharField(max_length=1000)),
                ('modeoftutor', models.CharField(max_length=20)),
                ('goalofchild', models.CharField(max_length=1000)),
                ('subjects', models.CharField(max_length=5000)),
                ('briefbio', models.TextField(max_length=3000)),
                ('curiculum', models.CharField(max_length=100)),
                ('typeoftutor', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=500)),
                ('state', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=14)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Start', models.CharField(max_length=100)),
                ('hrsperday', models.CharField(max_length=10)),
                ('starttime', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('duration', models.PositiveBigIntegerField(choices=[(1, '1 Day'), (7, '1 Week'), (30, '1 Month'), (90, '3 Months'), (180, '6 Months')])),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Educationalhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=800)),
                ('country', models.CharField(max_length=300)),
                ('start', models.CharField(max_length=300)),
                ('end', models.CharField(max_length=300)),
                ('course', models.CharField(max_length=500)),
                ('degrees', models.CharField(max_length=500)),
                ('grade', models.CharField(max_length=300)),
                ('tutor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.becometutor')),
            ],
        ),
        migrations.CreateModel(
            name='Activetutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires_in', models.DateField(auto_created=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('turorialkey', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='account.gettutor')),
            ],
        ),
    ]
