from django.shortcuts import render  
from django.http import HttpResponse  
  
def setsession(request):
    request.session['name']='amrit'
    request.session['class']='cse'
    return HttpResponse("chakko")
def getsession(request):
    studentname=request.session['name']
    studentclass=request.session['class']
    return HttpResponse(studentname+""+studentclass)
