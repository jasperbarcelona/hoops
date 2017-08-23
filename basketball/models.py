from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    msisdn = models.CharField(max_length=16)
    city = models.CharField(max_length=60)
    region = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    height = models.FloatField()
    average_rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class UserRating(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=60)
    rated_by_user_id = models.IntegerField()
    rated_by_user_name = models.CharField(max_length=60)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=30)
    wins = models.IntegerField()
    losses = models.IntegerField()
    city = models.CharField(max_length=60)
    region = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

class UserTeam(models.Model):
    user_id = models.IntegerField()
    team_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    STATUS_CHOICES = [
        ('open', 'open'),
        ('closed', 'closed'),
        ('ongoing', 'ongoing'),
        ('finished', 'finished'),
    ]
    TYPE_CHOICES = [
        ('private', 'Invite only'),
        ('public', 'Open for everyone')
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    court_id = models.IntegerField()
    court_name = models.CharField(max_length=60)
    date = models.DateTimeField()
    time = models.DateTimeField()
    created_by_user_id = models.IntegerField()
    created_by_user_name = models.CharField(max_length=60)
    game_type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

class UserGame(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('going', 'going'),
        ('declined', 'declined')
    ]
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    status = models.CharField(max_length=60, choices=STATUS_CHOICES)
    invited_by_user_id = models.IntegerField(default=None)
    invited_by_user_name = models.CharField(max_length=60, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

class Court(models.Model):
    name = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    region = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    image = models.TextField()
    added_by_user_id = models.IntegerField(default=None)
    added_by_user_name = models.CharField(max_length=60, default=None)
    verified_by_admin_id = models.IntegerField()
    verified_by_admin_name = models.CharField(max_length=60)
    verified = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)