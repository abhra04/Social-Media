from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Profile(ModelForm):
	class Meta:
		model = person
		fields = '__all__'
		exclude = ['unique_id','user']

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class makePost(ModelForm):
	class Meta:
		model = post 
		fields = ['userPerson','caption','picture']

class makeBlog(ModelForm):
	class Meta:
		model = blog
		fields = ['userPerson','content']

class followUser(ModelForm):
	class Meta:
		model = following
		fields = ['u1','u2']

class likes(ModelForm):
	class Meta:
		model = likes
		fields = ['poster','likegiver']