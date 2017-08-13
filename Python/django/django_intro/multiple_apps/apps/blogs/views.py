from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am your index"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create new blog"
    return HttpResponse(response)

def create(request):
    respose = "Create!"
    return redirect('/blogs')

def show(request, id):
    response = "Placeholder to display blog " + id
    return HttpResponse(response)

def edit(request, id):
    response = "Placeholder to edit blog " + id
    return HttpResponse(response)

def delete(request, id):
    response = "Destroy!"
    return redirect('/blogs')

def create1(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
