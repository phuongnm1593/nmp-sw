from django.db import models
from django.db.models import Q
import re
import random
import json
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

class Hero(models.Model):
    ASIA = 'asia'
    GLOBAL = 'global'
    SERVER_CHOICES = [
        (ASIA, ASIA),
        (GLOBAL, GLOBAL)
    ]

    name = models.CharField(max_length=255)
    race_name = models.CharField(max_length=255)
    server = models.CharField(max_length=8,choices=SERVER_CHOICES, default=ASIA)
    account_created_at = models.DateField()
    account_level = models.IntegerField(default=10)

    def __str__(self):
        return self.race_name


class Roll(models.Model):
    roll_date = models.DateTimeField()
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    ads_url= models.CharField(max_length=255, default="ads_short_url")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return "{date} - {hero}".format(date = self.roll_date.strftime("%Y-%m-%d"), hero= self.hero)

    def is_on(self):
        # roll_date = self.roll_date.replace(tzinfo=utc)

        # return self.is_active and datetime.now() < roll_date
        return self.is_active



class Candidate(models.Model):
    email = models.EmailField(max_length=255)
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[{roll}] {email}".format(roll=self.roll,  email=self.email)

class SessionKey(models.Model):
    key = models.CharField(max_length=64)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    expired_at = models.DateTimeField(default=datetime.now()+timedelta(minutes=15))

    def is_valid(self):
        # if self.is_expired():
        #     self.is_active = False
        #     return False
        return self.is_active
    
    def is_expired(self):
        return datetime.now() > self.expired_at

    def __str__(self):
        return "[{is_active}] [{expired_at}] {candidate}".format(is_active="Active" if self.is_active else "Inactive", expired_at = self.expired_at,  candidate=self.candidate)




