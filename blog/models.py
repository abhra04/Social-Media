from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class person(models.Model):
	user = models.OneToOneField(User,null=True, blank=True,on_delete = models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(null=True,blank=True,default="image1.jpg")
	unique_id = models.IntegerField(default = 0)
	def __str__(self):
		return self.name


class post(models.Model):

	profile_id = models.IntegerField(blank = False,default = 0)
	userPerson = models.ForeignKey(person, null=True, on_delete= models.SET_NULL)
	caption = models.CharField(max_length=20000,null=True,blank=True)
	picture =  models.ImageField(null=True,blank=True,default="image1.jpg")
	comments = models.CharField(max_length=20000,null=True,blank=True)


class blog(models.Model):

	profile_id = models.IntegerField(blank = False,default = 0)
	userPerson = models.ForeignKey(person, null=True, on_delete= models.SET_NULL)
	content = models.TextField(max_length=2000000,null=True,blank=True)
	likes = models.IntegerField(default = 0)
	comments = models.CharField(max_length=20000,null=True,blank=True)


class likes(models.Model):
	poster = models.ForeignKey(post, null=True, on_delete= models.SET_NULL)
	likegiver = models.ForeignKey(person, null=True, on_delete= models.SET_NULL)
	created = models.DateTimeField(auto_now_add=True)

class following(models.Model):
	u1= models.ForeignKey(person, null=True, on_delete= models.SET_NULL,related_name = 'follower')
	u2 = models.ForeignKey(person, null=True, on_delete= models.SET_NULL,related_name = 'followed')