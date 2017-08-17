from django.shortcuts import render, redirect
from places import items
import random


# Create your views here.
def index(request):
    context = {
        "items": items
    }
    if "gold" not in request.session:
        request.session['gold'] = 0

    if "activities" not in request.session:
        request.session['activities'] = []

    return render(request, "ninjaGold_app/index.html", context)

def randomizer(a, b):
    rand = random.randint(a, b)
    return rand

def process_money(request, id):
    for item in items:
        if int(id) == item['id']:
            newgold = randomizer(item['start'], item['end'])
            request.session['gold'] += newgold
    if newgold > 0:
        request.session['activities'].insert(0, {"comment":"You recieved {} gold".format(newgold)})
    if newgold < 0:
        request.session['activities'].insert(0, {"comment":"You lost {} gold".format(newgold)})
    return redirect('/')
