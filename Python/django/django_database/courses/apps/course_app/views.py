from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "course_app/index.html")

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    return render(request, "course_app/success.html")

def reg_process(request):
    errors = User.objects.registration_validator(request.POST)
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    request.session['user_id'] = errors
    return redirect('/success')


def logout(request):
    request.session.clear()
    return redirect('/')
