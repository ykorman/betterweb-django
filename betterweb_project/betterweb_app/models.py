from django.db import models
from django.contrib.auth.models import User

class Giver(models.Model):
    user = models.OneToOneField(User)
    # in cents
    wallet = models.PositiveIntegerField(default=0)
    # how much each "ding" is worth in cents
    ratio = models.PositiveIntegerField(default=5)
    anonymousDefault = models.BooleanField(default=False)

class Receiver(models.Model):
    user = models.OneToOneField(User)
    # in cents
    wallet = models.PositiveIntegerField(default=0)

class Deposit(models.Model):
    giver = models.ForeignKey(Giver)
    when = models.DateTimeField(auto_now_add=True)
    # in cents
    amount = models.PositiveIntegerField(default=0)

class Withdrawal(models.Model):
    receiver = models.ForeignKey(Receiver)
    when = models.DateTimeField(auto_now_add=True)
    # in cents
    amount = models.PositiveIntegerField(default=0)

class Tip(models.Model):
    giver = models.ForeignKey(Giver)
    receiver = models.ForeignKey(Receiver)
    when = models.DateTimeField(auto_now_add=True)
    # in cents
    amount = models.PositiveIntegerField(default=0)
    anonymous = models.BooleanField()