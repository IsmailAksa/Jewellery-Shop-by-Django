from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.utils import formats
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
   context={ 'variable1': 'this is sent', 
            'variable2': 'gibberish'
            }
   return render(request,'index.html', context)
    # return HttpResponse('this is home page')
def about(request):
  return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method=="POST":
      name=request.POST.get('name')
      email=request.POST.get('email')
      # password=request.POST.get('password')
      phone=request.POST.get('phone')
      
    
      contact=Contact(name=name,email=email,phone=phone)
      contact.save()
      messages.success(request, "Your Message has been sent!")
    return render(request,'contact.html')