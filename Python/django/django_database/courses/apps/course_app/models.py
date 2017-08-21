from __future__ import unicode_literals
from django.db import models
import re, bcrypt
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2: #or not postData['first_name'].isalpha():
            errors['name'] = "Input a name longer than 2 Characters"

        if len(postData['email']) < 2: # or not postData['first_name'].isalpha():
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

        today = datetime.datetime.today()
        if datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d") > today:
			errors['birthday']= "No future people allowed"

        if len(errors):
            return errors

        else:
            hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

            user = User.objects.create(
                name = postData['name'],
                email = postData['email'],
                password = hashed_pw,
                birthday = postData['birthday'],
                )

            return user.id


    def login_validator(self, postData):
        errors ={}

        if len(postData['email']) < 1:
            errors['login_email'] = "Enter an email"

        try:
            user = User.objects.get(email = postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['login_pass'] = "Incorrect Email/Password!"

        except:
            errors['login_val'] = "Login info incorrect!"

        if errors:
            return errors

        else:
            return user.id


class CourseManager(models.Manager):
    def course_validation(self, postData, id):
        errors = {}

        try:
            Course.objects.get(name = postData['name'])
            errors['duplicate'] = "Course already created!"

        except:
            pass

        if errors:
            return errors

        else:
            Course.objects.create(
                name=postData['name'],
                instructor = User.objects.get(id = id).name
                )

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Course(models.Model):
    name = models.CharField(max_length = 100)
    instructor = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    all_users = models.ManyToManyField(User, related_name = "all_courses")
    user = models.ForeignKey(User, related_name = "courses")

    objects = CourseManager()
