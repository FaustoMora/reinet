# Create your views here.
from django.shortcuts import render

def homeIncubaciones(request):
    return render(request,'base.tpl.html')
