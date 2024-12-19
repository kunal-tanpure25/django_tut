from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Admin - RUINER"
admin.site.site_title = "Ruiner portal"
admin.site.index_title = "Welcome to portal"

urlpatterns = [
    path('', views.index, name='home'),
    path('about',views.about , name = 'about'),
    path('contact', views.contact , name = 'contact'),
    path('signup', views.signup , name = 'signup'),
    path('form', views.form , name = 'form'),
    path('thanks', views.thanks, name = 'thanks'),
]