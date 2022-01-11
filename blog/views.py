from django.shortcuts import render,HttpResponse

# Create your views here.
def home(index):
    return HttpResponse("this is a home")

def blog(index):
    return HttpResponse("this is a blog")