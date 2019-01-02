from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    #my_dict = {'dynamic_content': "This is my dynamic content of DJango Application"}
    acc_rec = AccessRecord.objects.order_by('date')
    acc_rec_dict = {'access_record': acc_rec}
    return render(request, 'acc_rec.html', context = acc_rec_dict)
