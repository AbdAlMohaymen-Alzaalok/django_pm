from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Projectlistview.as_view(), name='Project_list'),
    path('project/create',views.ProjectCreateView.as_view(), name='Project_create')
]
