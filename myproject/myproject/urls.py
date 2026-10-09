"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from app import views, forms
import django.contrib.auth.views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from datetime import datetime
admin.autodiscover()

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view
)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout$', logout_view, name='logout'),
    re_path(r'register/', registration_view, name='register'),
    re_path(r'^account/$', account_view, name='account'),
    re_path(r'^booking$', views.bookings, name='bookings'),
    re_path(r'^sessions$', views.sessions, name='sessions'),
    re_path(r'^payment$', views.payment, name='payment'),
    re_path(r'^progressreport$', views.progressreport, name='progressreport'),
    re_path(r'^chat$', views.chat, name='chat'),
    re_path(r'^assignments$', views.assignments, name='assignments'),
    re_path(r'^classes$', views.classes, name='classes'),
    re_path(r'^resources$', views.resources, name='resources'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
     
   
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='account/registration/password_reset_form.html',
        email_template_name='account/registration/password_reset_email.html',
        subject_template_name='account/registration/password_reset_subject.txt'
    ), name='password_reset'),
    
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)