from django.shortcuts import render
from basic_app import forms
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

def form_detail(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("The Submitted Value(s) are: ")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Address: " + form.cleaned_data['address'])

    return render(request, 'basic_app/form_template.html', {'form_content': form})
