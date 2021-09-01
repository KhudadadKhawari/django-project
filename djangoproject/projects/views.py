from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    # return HttpResponse('This is the Multiple Projects page')
    return render(request, 'projects.html')

def project(request):
    # return HttpResponse('This is a single project page')
    return render(request, 'single-project.html')

# Create your views here.
