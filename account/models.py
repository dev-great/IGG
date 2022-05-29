from math import degrees
import profile
from pyexpat import model
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
from django.forms import DateField
from .choices import *
from datetime import timedelta
from datetime import datetime as dt
from tutorial.models import TutorModel
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

from cloudinary.models import CloudinaryField

today = datetime.date.today()


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    phonenumber = models.CharField(
        max_length=20, blank=True, default=False, null=True)
    fullname = models.CharField(
        max_length=500, blank=True, default=False, null=True)
    address = models.TextField(
        max_length=5000, blank=True, default=False, null=True)
    profilepix = CloudinaryField('image', resource_type = "image",)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class Becometutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    newsletters = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=15)
    whatsappnumber = models.CharField(max_length=15)
    dob = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    primarylanguage = models.CharField(max_length=100)
    countryofresidency = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    region = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    address = models.TextField(max_length=500)
    teachingmode = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Educationalhistory(models.Model):
    tutor = models.ForeignKey(
        Becometutor, on_delete=models.CASCADE, default=None)
    school = models.CharField(max_length=800)
    country = models.CharField(max_length=300)
    start = models.CharField(max_length=300)
    end = models.CharField(max_length=300)
    specialty = models.CharField(max_length=500)
    course = models.CharField(max_length=500)
    degrees = models.CharField(max_length=500)
    grade = models.CharField(max_length=300)

    def __str__(self):
        return self.tutor.email


class Workhistory(models.Model):
    tutor = models.ForeignKey(
        Becometutor, on_delete=models.CASCADE, default=None)
    organization = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    start = models.CharField(max_length=300)
    stop = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    teachingrole = models.BooleanField(default=False)
    stillactive = models.BooleanField(default=False)

    def __str__(self):
        return self.tutor.email


class KYC(models.Model):
    tutor = models.ForeignKey(
        Becometutor, on_delete=models.CASCADE, default=None)
    passportphoto = CloudinaryField('image', resource_type = "image",)
    valiedid = CloudinaryField('image', resource_type = "image",)
    introvideo = CloudinaryField('videos', resource_type = "video", chunk_size = 200000000,)

    def __str__(self):
        return self.tutor.email


class Gettutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    kidsnum = models.CharField(max_length=50)
    classofkid = models.CharField(max_length=3000)
    modeoftutor = models.CharField(
        max_length=100)
    goalofchild = models.CharField(
        max_length=1000)
    subjects = models.CharField(max_length=5000)
    briefbio = models.TextField(max_length=3000)
    curiculum = models.CharField(
        max_length=500)
    typeoftutor = models.CharField(
        max_length=100)
    address = models.TextField(max_length=1000)
    state = models.CharField(max_length=1000)
    bustop = models.CharField(max_length=1000)
    phonenumber = models.CharField(max_length=15)
    fullname = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    Start = models.CharField(
        max_length=100)
    hrsperday = models.CharField(
        max_length=10)
    starttime = models.CharField(
        max_length=500)
    timestamp = models.DateTimeField(auto_now=True)
    duration = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username


@ receiver(post_save, sender=Gettutor)
def payment_ammount(sender, instance, *args, **kwargs):
    if instance.duration == 1:
        Activetutor.objects.create(turorialkey=instance, amount=1600.00,
                                   expires_in=datetime.datetime.strptime(instance.Start, "%Y-%m-%d").date() + timedelta(days=instance.duration))
    elif instance.duration == 7:
        Activetutor.objects.create(turorialkey=instance, amount=11200.00,
                                   expires_in=datetime.datetime.strptime(instance.Start, "%Y-%m-%d").date() + timedelta(days=instance.duration))
    elif instance.duration == 30:
        Activetutor.objects.create(turorialkey=instance, amount=48000.00,
                                   expires_in=datetime.datetime.strptime(instance.Start, "%Y-%m-%d").date() + timedelta(days=instance.duration))
    elif instance.duration == 90:
        Activetutor.objects.create(turorialkey=instance, amount=144000.00,
                                   expires_in=datetime.datetime.strptime(instance.Start, "%Y-%m-%d").date() + timedelta(days=instance.duration))
    elif instance.duration == 180:
        Activetutor.objects.create(turorialkey=instance, amount=288000.00,
                                   expires_in=datetime.datetime.strptime(instance.Start, "%Y-%m-%d").date() + timedelta(days=instance.duration))
    else:
        Activetutor.objects.create(turorialkey=instance, amount=1600.00,
                                   expires_in=datetime.datetime.strptime(instance.Start, "%Y-%m-%d").date() + timedelta(days=instance.duration))


class Activetutor(models.Model):
    turorialkey = models.ForeignKey(
        Gettutor, related_name='status', on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    expires_in = models.DateField(null=True, auto_created=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.turorialkey.user.username


@ receiver(post_save, sender=Activetutor)
def expiring_date(sender, instance, *args, **kwargs):
    if instance.expires_in == today:
        turorialkey = Activetutor.objects.get(id=instance.id)
        turorialkey.delete()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    referenceCode = models.CharField(max_length=100, default='', blank=True)
    paystackAccessCode = models.CharField(
        max_length=100, default='', blank=True)
    paymentFor = models.ForeignKey(
        TutorModel, on_delete=models.CASCADE, default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    duration = models.PositiveBigIntegerField(default=30)

    def __str__(self):
        return self.user.username


@ receiver(post_save, sender=Payment)
def create_subscription(sender, instance, *args, **kwargs):
    if instance:
        Subscription.objects.create(subscriber=instance, expires_in=dt.now(
        ).date() + timedelta(days=instance.duration))


# User Subscription
class Subscription(models.Model):
    subscriber = models.ForeignKey(
        Payment, related_name='subscription', on_delete=models.CASCADE, default=None)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subscriber.user.username


@ receiver(post_save, sender=Subscription)
def update_active(sender, instance, *args, **kwargs):
    if instance.expires_in == today:
        subscription = Subscription.objects.get(id=instance.id)
        subscription.delete()


@ receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}, here is your password reset token: {} Copy and past in your app".format(
        reset_password_token.user.username, reset_password_token.key,)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        fail_silently=False
    )
