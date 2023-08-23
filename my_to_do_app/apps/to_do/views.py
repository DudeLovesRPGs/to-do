from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils import timezone
from apps.to_do.models import Todo

# Create your views here.
def index(request):

    return render(request, 'to_do/index.html')

@csrf_protect
def add_todo(request):
    done_by = timezone.now()
    content = request.POST['content']
    new_todo = Todo.objects.create(added_date = done_by, text = content)
    return render(request, 'to_do/index.html')