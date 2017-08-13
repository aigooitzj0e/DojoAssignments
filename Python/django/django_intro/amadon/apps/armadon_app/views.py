from datetime import datetime
from django.shortcuts import render, redirect
from inventory import items #imported the items dictionary from inventory.py

def index(request):
    context = {
        'items': items #items is the dictionary name in inventory and items are the items within the dictionary.
    }
    return render(request, "armadon_app/index.html", context)


def process(request, id):
    for item in items: #iterates through each item in 'items' dictionary. (item is the element)

        print "this is the item name inside our items dictionary:", item['name']
        print "this is item id inside our items dictionary:", item['id']

        #We need to compare our item['id'] from the dictionary to the id the form is giving out
        if item['id'] == int(id): # add int to convert the string id into an integer.
            print "matched item['id'] from dictionary to form id"
            cost = item['price'] * int(request.POST['quantity']) #multiply the item['price'] to the quantity selected in the form.
            print "the cost is:", cost

    request.session['cost'] = cost #made cost into sessions to pass it into the checkout page

    if "count" not in request.session: #this sets request.session['count'] to a variable and sets it to a starting point of 0
        request.session['count'] = 0
    request.session['count'] += int(request.POST['quantity']) #keeps a sum of the count depending on what is chosen in the quanitity form

    if "totalamount" not in request.session: #makes totalamount a session and set to 0
        request.session['totalamount'] = 0
    request.session['totalamount'] += cost #sum of cost (cost is declared on line 22)

    return redirect('/checkout') # does logic on /process and redirects to /checkout which renders checkout.html


def checkout(request):
    return render(request, "armadon_app/checkout.html")
