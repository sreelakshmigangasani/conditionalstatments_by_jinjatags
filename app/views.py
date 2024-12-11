from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'name':'Lakshmi','a':20}
    return render(request,'conditions.html',context=d)