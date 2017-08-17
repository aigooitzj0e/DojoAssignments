from __future__ import unicode_literals
from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Input a name longer than 2 Characters"
        if len(postData['email']) < 2:
            errors['email'] = "Enter an email"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be 8 characters minimum"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords do not match!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['pass'] = "Invalid email address"

        try:
            User.objects.get(email = postData['email'])
            errors['duplicate'] = "Email already registered"

        except:
            pass

        if len(errors):
            return errors
        else:
            hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

            user = User.objects.create(
                name = postData['name'],
                email = postData['email'],
                password = hashed_pw
                )
            return user.id








class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()











def reg_validator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors['first_name'] = "Oops, your first name needs to be longer"
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
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
