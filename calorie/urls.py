"""
URL configuration for calorie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tracker import views
from django.contrib import admin

app_name = 'calorie_counter'

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', views.food_list, name='food_list'),
    path('add/', views.add_food, name='add_food'),
    path('view/', views.view_calories, name='view_calories'),
]

