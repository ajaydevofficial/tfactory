"""ecommerce URL Configuration

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
from django.urls import path
from .views import home_page,login_page,register_page,soon_page,talent_page,technical_page,clothes_page,design_order_page
from .views import privacy_page,return_page,project_order_page,portrait_order_page,kurta_store_page,web_order_page,terms_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name="Home_Page"),
    path('home/',home_page,name="Home_Page"),
    path('login/',login_page,name="Login_Page"),
    path('register/',register_page,name="Register_Page"),
    path('soon/',soon_page,name="Soon_Page"),
    path('talent/',talent_page,name="Talent_Page"),
    path('technical/',technical_page,name="Technical_Page"),
    path('clothes/',clothes_page,name="Clothes_Page"),
    path('design/',design_order_page,name="Design_Order_Page"),
    path('privacy/',privacy_page,name="Privacy_Page"),
    path('return/',return_page,name="Return_Page"),
    path('project/',project_order_page,name="Project_Order_Page"),
    path('portrait/',portrait_order_page,name="Portrait_Order_Page"),
    path('kurta/',kurta_store_page,name="Kurta_Store_Page"),
    path('web/',web_order_page,name="Web_Order_Page"),
    path('terms/',terms_page,name="Terms_Page"),

]
