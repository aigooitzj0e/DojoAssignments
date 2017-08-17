# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models

import re
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Did you forget your first name?"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Did you forget your last name?"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email is invalid"
        return errors;

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
