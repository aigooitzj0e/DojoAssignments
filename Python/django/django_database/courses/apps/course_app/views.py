from django.shortcuts import render, redirect
from .models import User, Course
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "course_app/index.html")


def dashboard(request):
    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all(),
        "welcome": User.objects.get(id = request.session['user_id']),
        "enrolled": Course.objects.filter(all_users__id = request.session['user_id'] ),
        "teaching": Course.objects.filter(user__id = request.session['user_id']),
    }
    try: #checks is user is logged in.
        request.session['user_id']
    except KeyError:
        return redirect('/')
    return render(request, "course_app/dashboard.html", context)


def teach(request):
    try: #checks is user is logged in.
        request.session['user_id']
    except KeyError:
        return redirect('/')

    context = {
        "users": User.objects.all(),
    }
    return render(request, "course_app/teach.html", context)


def teach_process(request, id):
    if request.method == 'POST':
        errors = Course.objects.course_validation(request.POST, id)
        if type(errors) == dict:
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/teach')
        return redirect('/dashboard')
    else:
        messages.error("You dont have permission to that awesome page!")


def enroll(request):
    try: #checks is user is logged in.
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all(),
    }
    return render(request, "course_app/enroll.html", context)


def enroll_process(request, cid):
    User.objects.get(id=request.session['user_id']).all_courses.add(Course.objects.get(id=cid))
    return redirect('/dashboard')


def reg_process(request):
    errors = User.objects.registration_validator(request.POST)
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    request.session['user_id'] = errors
    return redirect('/dashboard')


def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    request.session['user_id'] = errors
    return redirect('/dashboard')


def delete(request, id):
    courseDelete = Course.objects.get(id = id)
    courseDelete.delete()
    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')
