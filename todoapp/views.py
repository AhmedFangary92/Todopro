from django.shortcuts import render
from .models import *
import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')


def list(request):
    mydectionary = {
        'todolist' : Todo.objects.all()
    }
    return render(request, 'list.html', context=mydectionary)


def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    mydectionary = {
        'todolist' : Todo.objects.all()
    }
    return render(request, 'list.html', context=mydectionary)


def delete(request, id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydectionary = {
        'todolist' : Todo.objects.all()
    }

    return render(request, 'list.html', context=mydectionary)


def edit(request, id):
    obj = Todo.objects.get(id=id)
    mydectionary = {
        'id' : obj.id,
        'title' : obj.title,
        'description' : obj.description,
        'priority' : obj.priority
    }

    return render(request, 'edit.html', context=mydectionary)


def sortdata(request):
    mydectionary = {
        'todolist' : Todo.objects.all().order_by('priority')
    }

    return render(request, 'list.html', context=mydectionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        'todolist' : Todo.objects.filter(title__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

def update(request, id):
    
    updated_at = datetime.datetime.now()
    
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.created_at = updated_at
    obj.save()

    mydectionary = {
        'todolist' : Todo.objects.all()
    }
    return render(request, 'list.html', context=mydectionary)