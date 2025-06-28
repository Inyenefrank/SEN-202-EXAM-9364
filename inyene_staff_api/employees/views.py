from django.shortcuts import render
from .models import post


def home(request):
    posts = post.objects,all().order_by('created_at')
    return render(request,'employees/home.html',{'posts':posts})

def manager(request):
    posts = post.objects,all()
    return render(request,'employees/manager.html',{'posts':posts})

def intern(request):
    posts = post.objects,all()
    return render(request,'employees/intern.html',{'posts':posts})


# Create your views here.
