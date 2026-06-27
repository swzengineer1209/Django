from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello World!. You are on Home page now!')
    # return render(request,'index.html')
    return render(request,'website/index.html')

def about(request):
    return HttpResponse('Hello World!. You are on About page now!')

def contact(request):
    return HttpResponse('Hello World!. You are on Contact page now!')






