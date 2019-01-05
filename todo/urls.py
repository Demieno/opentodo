"""opentodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles import views as static_views
from django.urls import re_path, path
from django.views.static import serve
from .views import *

urlpatterns = [
    path('', index),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #re_path(r'^static/(.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += [
    path('tasks/', list, name='tasks_list'),
    re_path(r'^tasks/new/$', add_task, name='add_task'),
    re_path(r'^tasks/(?P<task_id>\d+)/comments/new/$', add_comment, name='add_comment'),
    re_path(r'^tasks/delete_comment/(?P<comment_id>\d+)/$', del_comment, name='del_comment'),
    re_path(r'^tasks/(?P<task_id>\d+)/$', details, name='task_details'),
    re_path(r'^tasks/(?P<task_id>\d+)/edit/$', edit, name='edit_task'),
    re_path(r'^tasks/(?P<task_id>\d+)/delete/$', delete, name='delete_task'),
    re_path(r'^tasks/(?P<task_id>\d+)/to_accepted/$', task_to_accepted, name='task_to_accepted'),
    re_path(r'^tasks/(?P<task_id>\d+)/to_done/$', task_to_done, name='task_to_done'),
    re_path(r'^tasks/(?P<task_id>\d+)/to_checked/$', task_to_checked, name='task_to_checked'),
    re_path(r'^tasks/(?P<task_id>\d+)/to_new/$', task_to_new, name='task_to_new'),
    re_path(r'^tasks/delete_attach/(?P<attach_id>\d+)/$', delete_task_attach, name='delete_task_attach'),

    re_path(r'^projects/$', projects_list, name='projects_list'),
    re_path(r'^projects/new/$', add_project, name='add_project'),
    re_path(r'^projects/(?P<project_id>\d+)/$', project_details, name='project_details'),
    re_path(r'^projects/(?P<project_id>\d+)/edit/$', edit_project, name='edit_project'),
    re_path(r'^projects/(?P<project_id>\d+)/delete/$', delete_project, name='delete_project'),
    re_path(r'^projects/delete_attach/(?P<attach_id>\d+)/$', delete_project_attach, name='delete_project_attach'), 

    re_path(r'^json/project_users/$', json_project_users, name='json_project_users'), 
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static_views.serve),
    ]
