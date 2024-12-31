from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

# Dynamic refrencing for the user model 
User = get_user_model()

class CustomUser(AbstractUser):
    ...
    def __str__(self):
        return self.username
    
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