from django.contrib import admin
from django.urls import path, include, re_path

#from ssoauth import views as ssoauth_views
from .views import *

urlpatterns = [

    path('admin/', admin.site.urls),
  #  re_path(r"^(?:\w+/)?login/?$", ssoauth_views.LogInView.as_view(already_authenticated_403=True)),
   # re_path('', include('ssoauth.urls')),


    path('', FormViewPage.as_view(), name='home'),
    path('formular/', IncidentFormPage.as_view(), name='form'),
    path('update/<int:pk>/', IncidentFormUpdatePage.as_view(), name='update'),
    path('delete/<int:pk>/', IncidentFormDeletePage.as_view(), name='delete'),


]

