from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    about = About.objects.all().get()
    skills = Skill.objects.all().order_by('id')
    works = RecentWork.objects.all()
    return render(request,'home.html',{'about':about,'skills':skills,'works':works})