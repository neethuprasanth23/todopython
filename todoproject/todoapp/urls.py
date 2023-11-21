from django.urls import path

# import todoapp
from . import views
# app_name=todoapp

urlpatterns = [
    path('', views.add, name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:taskid>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),

]
