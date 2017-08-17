from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import re
# Create your views here.
def index(request):
    context = {
        "users": User.objects.all(),
    }
    return render(request, "SRU_app/index.html", context)

def new(request):
    return render(request, "SRU_app/new.html")

def edit(request, idd):
    context = {
        'user': User.objects.get(id=idd)
    }
    return render(request, 'SRU_app/edit.html', context)

def edit_process(request, idd):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/edit')

    updateUser = User.objects.get(id = idd)
    updateUser.first_name = request.POST['first_name']
    updateUser.last_name = request.POST['last_name']
    updateUser.email = request.POST['email']
    updateUser.save()
    return redirect('/')

def new_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/new')

    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
    )

    return redirect('/')

def show(request, idd):
    context = {
        'user': User.objects.get(id = idd)
    }
    return render(request, 'SRU_app/show.html', context)

def delete(request, idd):
    userDelete = User.objects.get(id = idd)
    userDelete.delete()
    return redirect('/')
