from django.shortcuts import render
from forms import *
from django.forms.formsets import formset_factory
from django import forms
from django.forms import modelformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.



def index(request):
    return render(request,'index.html')



def login(request):
	form= LoginForm()
	if request.method == 'POST':
		email = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(email=email, password=password)
		if user:
		   
			login(request, user)
			users = Users.objects.all().filter(user=user.id).order_by('id') 
			for x in users :
			    id_u=x.id
			#__setitem__("user_session", request)	
			request.session['user'] = user.email
			request.session['user_id'] = id_u
			request.session['active'] = 1
			return render(request, 'index.html')
		   
		else:
			print "Invalid login details: {0}, {1}".format(email, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'login.html',{'form':form})




def registration(request):
    return render(request,"registration.html")
