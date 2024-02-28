from django.http import HttpResponse
from django.shortcuts import render

data = {
    'squirrels' : [
        {
            'name' : 'Jimmy',
            'weight' : 10,
            'image' : 'IMAGE'
        },
        {
            'name' : 'Squeak',
            'weight' : 7,
            'image' : 'IMAGE'
        },
        {
            'name' : 'Lucky',
            'weight' : 6,
            'image' : 'IMAGE'
        }
    ]
}

def home(request):
    return render(request, 'home/home.html', data)

def create(request):
    return render(request, 'create/create.html', {'data' : "CREATE"})

def read(request):
    return render(request, 'read/read.html', data)

def update(request):
    return render(request, 'update/update.html', {'data' : "UPDATE"})

def delete(request):
    return render(request, 'delete/delete.html', {'data' : "DELETE"})

