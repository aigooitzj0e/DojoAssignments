from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    
    def reg_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors['first_name'] = "Oops, your first name needs to be longer"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Oops, your last name needs to be longer"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email is invalid"
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be 8 characters minimum"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Your passwords don't match!"
        try:
            User.objects.get(email = postData['email'])
            errors['duplicate'] = "Email already registered"
        except:
            pass
        return errors;

    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email_login'] = "Enter a valid email"
        try: #no error
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['login_pass'] = "Login info incorrect"
        except: #with error
            errors['login_val'] = "Login info incorrect"
        if errors:
            return errors
        return user.id

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
