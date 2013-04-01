# Create your views here.
from models import todo														# Remember we had created a class called "todo" in models.py inside this app
from django.shortcuts import render_to_response

def mb_index(request): 							#Define our function, accept a request

    items = todo.objects.all() 			#ORM queries the database for all of the to-do entries.

    return render_to_response('index.html', {'items': items}) # Responds with passing the object items (contains info from the DB) to the template index.html

