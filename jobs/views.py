from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.

def home(request):
    try:
        about = About.objects.get()
        skills = Skill.objects.all().order_by('id')
        works = RecentWork.objects.all()
    except:
        pass
    return render(request,'home.html',{'about':about,'skills':skills,'works':works})

def saveContact(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return HttpResponseRedirect(reverse('home'))