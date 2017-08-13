from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, "random_app/index.html")

def reset(request):
    #reset session here
    return redirect('/')

def generate(request):
    # if request.method == 'POST':

    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
		# return render_template('index.html', counter=session['counter'])

    # request.session['count'] = request.session['count'] + 1

    context = {
        "randomWord": get_random_string(length=14),
    }

    return render(request, "random_app/index.html", context)
