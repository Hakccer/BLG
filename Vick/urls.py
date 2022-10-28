from django.contrib import admin
from django.urls import path, include
from Vick import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs', views.blogs, name="Blogs"),
    path('blogs/<slug:slug>/', views.Blogposts)
]
