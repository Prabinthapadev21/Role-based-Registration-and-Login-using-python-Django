from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('admin/',views.admin_page,name='admin'),
    path('employee/',views.employee_page,name='employee'),
    path('customer/',views.customer_page,name='customer'),
    path('logout/',views.logout_view,name='logout'),
]