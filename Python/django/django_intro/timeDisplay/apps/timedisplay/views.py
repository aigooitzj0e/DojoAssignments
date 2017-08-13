from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
    "time": strftime("%B %d, %Y %I:%M %p", gmtime())
    }
    return render(request,"timedisplay/index.html", context)
