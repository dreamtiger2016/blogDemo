#-*- coding: UTF-8 -*-   
from django.shortcuts import render, render_to_response
from django.template import loader, Context,RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost
from django import forms
from models import User


def archive(req):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))


class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单的用户名密码数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加用户到数据库中
            User.objects.create(username= username,password=password)
            #跳转到主页
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect('/blog/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/blog/login/')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #跳转到主页
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect('/blog/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/blog/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))


#登录、注册后跳转到主页
def index(req):
    username = req.session.get('username','')
    posts = BlogPost.objects.all()
    return  render_to_response('index.html',{'username':username,'posts':posts})
