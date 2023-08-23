from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils import timezone
from apps.to_do.models import Todo

# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'to_do/index.html', {
        "todos": todo_items
    })

@csrf_protect
def add_todo(request):
    done_by = timezone.now()
    content = request.POST['content']
    new_todo = Todo.objects.create(added_date = done_by, text = content)
    return HttpResponseRedirect("/todo/")