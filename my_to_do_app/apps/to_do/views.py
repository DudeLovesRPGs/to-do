from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):

    return render(request, 'to_do/index.html')


def add_todo(request):
    print(request.POST)
    print("Added to-do;Redirecting to home")
    return render(request, 'to_do/index.html')