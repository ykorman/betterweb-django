from django.db import models
from django.contrib.auth.models import User

class Giver(models.Model):
    user = models.OneToOneField(User)
    # in cents
    wallet = models.PositiveIntegerField(default=0)
    # how much each "ding" is worth in cents
    ratio = models.PositiveIntegerField(default=5)
    anonymousDefault = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.user.username

class Receiver(models.Model):
    user = models.OneToOneField(User)
    # in cents
    wallet = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return self.user.username

class Deposit(models.Model):
    giver = models.ForeignKey(Giver)
    when = models.DateTimeField(auto_now_add=True)
    # in cents
    amount = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return u"%s deposited %d" % (self.giver.user.username, self.amount)

class Withdrawal(models.Model):
    receiver = models.ForeignKey(Receiver)
    when = models.DateTimeField(auto_now_add=True)
    # in cents
    amount = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return u"%s withdrawn %d" % (self.receiver.user.username, self.amount)

class Tip(models.Model):
    giver = models.ForeignKey(Giver)
    receiver = models.ForeignKey(Receiver)
    when = models.DateTimeField(auto_now_add=True)
    # in cents
    amount = models.PositiveIntegerField(default=0)
    anonymous = models.BooleanField()
    
    def __unicode__(self):
        return u"%s gave %d to %s" % (self.giver.user.username, self.receiver.user.username, amount)

class Art(models.Model):
    owner = models.ForeignKey(Receiver)
    link = models.URLField()
    
    def __unicode__(self):
        return u"%s owns %s" % (self.owner.user.username, self.link)

class TipToArt(models.Model):
    giver = models.ForeignKey(Giver)
    link = models.URLField()
    
    def __unicode__(self):
        return u"%s gave to %s" % (self.giver.user.username, self.link)
