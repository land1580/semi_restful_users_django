from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors["first_name"] = "FIRST NAME TOO SHORT!  -Please re-enter your first name"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = "LAST NAME TOO SHORT!  -Please re-enter your last name"
        if not EMAIL_REGEX.match(post_data['email']):
            errors["email"] = "INVALID EMAIL!  -Please enter valid email (Ex. email@gmail.com)"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()