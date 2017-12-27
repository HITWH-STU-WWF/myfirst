from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello word')

def home_temp(request):
    #render函数接收多个参数，其中第一个参数（收到的请求）和第二个参数（返回的模板路径）为必填参数，剩余的为可选
    return render(request,'firstapp/home.html',{'name':'hello, wwf'})