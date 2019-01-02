from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello DJango Refresher App</h1>")
    my_dict = {'insert_me': 'This is the Dynamic portion of my application'}
    return render(request, 'refresher_app/index.html', context = my_dict)
