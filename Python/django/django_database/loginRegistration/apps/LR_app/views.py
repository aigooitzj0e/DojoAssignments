from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "LR_app/index.html")

def results(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    return render(request, "LR_app/results.html")

def reg_process(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    print hashed_pw

    logged = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password = hashed_pw,
    )

    request.session['user_id'] = logged.id
    return redirect('/results')


def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    if type(errors) == int:
        request.session['user_id'] = errors
        return redirect ('/results')

def logout(request):
    request.session.clear()
    return redirect('/')
