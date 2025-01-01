from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=150, null=True, blank=True)
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=150, null=True)
    team = models.CharField(max_length=150, null=True)
    birthday = models.DateField(null=True)
    start_date = models.DateField(null=True)
    role = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.username
    
# Dynamic refrencing for the user model 
User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, related_name='custom_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #   This is for future enhancement: dynamic group population
    #   criteria = models.JSONField(blank=True, null=True)  # Example: {"gender": "female"}
    # def update_members(self):
    # if self.criteria:
    #     # Example: Select all female employees
    #     from django.db.models import Q
    #     matching_users = User.objects.filter(**self.criteria)
    #     self.members.set(matching_users)

    def __str__(self):
        return self.name