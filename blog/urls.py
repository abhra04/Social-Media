from django.urls import path
from . import views


urlpatterns = [
	#path('register/', views.registerPage, name="register"),
	#path('login/', views.loginPage, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
    path('', views.homePage, name="homePage"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('profile/<str:pk_test>/', views.userProfile, name="userProfile"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.profileSettings, name="account"),
    path('profileView/', views.profileView, name="profileView"),
    path('reloadWall/', views.reloadWall, name="reloadWall"),
    path('createPost/', views.createPost, name="createPost"),
    path('createBlog/', views.createBlog, name="createBlog"),
    path('followUser/', views.followingUser, name="followUser"),
   



]