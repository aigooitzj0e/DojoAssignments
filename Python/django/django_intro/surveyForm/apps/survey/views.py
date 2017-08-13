from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def results(request):
    return render(request, 'survey/results.html')

def process(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['lang'] = request.POST['lang']
    request.session['comment'] = request.POST['comment']


    return redirect('/results')
