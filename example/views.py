from django.shortcuts import render
from django.http import HttpResponse
from  .models import student


def index(request):
    return render(request,"home.html")

def add(request):
    v1=int(request.POST['n1'])
    v2=int(request.POST['n2'])
    res=v1+v2
    return render(request,"result.html",{'result1':res})

def test(request):
    return render(request,"result2.html")  

def std(request):
    st1=student.objects.all()
    
    return render(request,'result2.html',{'result':st1})


def test2(request):
    return render(request,"test1.html")  


def DB1(request):


    name1=request.POST['n1']
    age1=request.POST['n2']

    res=student(name=name1,age=age1)
    res.save()

    return render(request,'home.html')
