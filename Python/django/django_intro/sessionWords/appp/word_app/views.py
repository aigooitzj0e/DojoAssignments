from datetime import datetime
from django.shortcuts import render, redirect

def index(request):
    return render(request, "word_app/index.html")

def add(request):
    new_word = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "show-big":
            new_word[key] = value
        if key == "show-big":
            new_word['big'] = "big"
        else:
            new_word['big'] = ""
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.insert(0, new_word)
    request.session['words'] = temp_list

    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
