"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include

from todo_project.main_view import Index
from todos.views import TodoList
from todos.views import TodoDetails

urlpatterns = [
    path('', Index.as_view()),  # Changed from '/' to '' for the root path
    path('admin/', admin.site.urls),
    path('todo/', TodoList.as_view(), name='todo_list'),
    path('todo/<int:pk>/', TodoDetails.as_view(), name='todo_details'),
]
