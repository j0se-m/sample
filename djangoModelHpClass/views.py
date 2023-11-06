from django.shortcuts import render
from djangoModelHpClass.forms import WanafunziForm


def home(request):
    stud = WanafunziForm()

    return render(request, 'index.html', {'form': stud})
