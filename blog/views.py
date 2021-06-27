from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required

def homePage(request):
	return render(request,'blog/home.html')

def loginPage(request):
	return render(request,'blog/login.html')

def registerPage(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST,request.FILES)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			person.objects.create(
				user=user,
				name=user.username,
				unique_id = user.id
				)

			
			
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
	context = {'form':form}
	return render(request,'blog/register.html',context)
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			idx = request.user.id
			return redirect( '/profile/' + str(idx))
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'blog/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
@login_required(login_url = 'login')
def profileSettings(request):
	person = request.user.person
	form = Profile(instance=person)
	if request.method == 'POST':
		form = Profile(request.POST, request.FILES,instance=person)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request, 'blog/account_settings.html', context)
@login_required(login_url = 'login')
def userProfile(request, pk_test):
	user = person.objects.get(unique_id=pk_test)	
	followingUsers = request.user.person.follower.all()
	context = {'user':user,'followingUsers' : followingUsers}
	return render(request, 'blog/profilepage.html',context)
@login_required(login_url = 'login')
def profileView(request):
	user = request.user.person
	posts = request.user.person.post_set.all()
	blogs = request.user.person.blog_set.all()
	context = {'user':user,'posts': posts,'blogs':blogs}
	print(posts)
	return render(request, 'blog/profileView.html',context)
@login_required(login_url = 'login')
def reloadWall(request):
	user = request.user.person
	idx = user.unique_id
	return redirect('http://127.0.0.1:8000/profile/' + str(idx))


@login_required(login_url = 'login')
def createPost(request):
	people = request.user.person
	idx = people.unique_id
	print(idx)
	data = {'profile_id': idx,'userPerson': people}
	form = makePost(initial = data)
	if request.method == 'POST':
		form = makePost(request.POST,request.FILES,initial= data)
		if form.is_valid():
			form.save()
			return redirect('http://127.0.0.1:8000/profile/' + str(idx))
	context = {'form':form}
	return render(request,'blog/createPost.html',context)


@login_required(login_url = 'login')
def createBlog(request):
	people = request.user.person
	idx = people.unique_id
	print(idx)
	data = {'profile_id': idx,'userPerson': people}
	form = makeBlog(initial = data)
	if request.method == 'POST':
		form = makeBlog(request.POST,request.FILES,initial= data)
		if form.is_valid():
			form.save()
			return redirect('http://127.0.0.1:8000/profile/' + str(idx))
	context = {'form':form}
	return render(request,'blog/createBlog.html',context)
@login_required(login_url = 'login')
def followingUser(request):
	people = request.user.person
	idx = people.unique_id
	data = {'u1':people}
	people_you_are_following = request.user.person.follower.all()
	form1 = followUser(initial = data)
	if request.method == 'POST':
		form1 = followUser(request.POST,request.FILES,initial= data)
		if form1.is_valid():
			form1.save()
			return redirect('http://127.0.0.1:8000/profile/' + str(idx))
	context = {'form':form1,'people_you_are_following':people_you_are_following }
	return render(request,'blog/followUser.html',context)






