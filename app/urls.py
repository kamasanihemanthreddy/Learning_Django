
from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('gcal/', views.googlecal_auth, name='google_calander'),
    path('upload/', views.fileupload, name='upload'),
    path('display/',views.display_upload_data, name='display'),
    
]
