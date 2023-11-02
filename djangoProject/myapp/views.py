from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import   Projects, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'index.html')

def hello(request,userName):
    print(userName)
    return HttpResponse("<h1 style='color:white; background:black; text-align:center;'>Hello "+userName.capitalize()+"</h1>")

def about(request):
    return HttpResponse("<h1 style='color:white; background:black; text-align:center;'>ABOUT</h1>")

def projects(request):
    projects =list( Projects.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, descriptionn):
    task= get_object_or_404(Task,description__contains=descriptionn)
    
    return JsonResponse(task.title, safe=False)