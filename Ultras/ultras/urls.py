"""
URL configuration for ultras project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ultrasapp.views import *
from admin_app.views import *

urlpatterns = [

    # Website 

    path('',index),
    path('about/',about),
    path('blogmansonry/',mansonry),
    path('blogsidebar/',sidebar),
    path('blog/',blog),
    path('cart/',cart),
    path('checkout/',check),
    path('comingsoon/',coming),
    path('contact/',contact),
    path('error/',error),
    path('faqs/',faqs),
    path('login/',login),
    path('shopgrid/',grid),
    path('shop-list/',list),
    path('shop-slider/',slider),
    path('shop/',shop),
    path('single-post/',single_post),
    path('single-product/',single_product),
    path('styles/',styles),
    path('thank-you/',thanks),
    path('wishlist/',wishlist),


    # Admin_app URLS.....
   
    path('login/',log),
    path('ct/',ct),
    path('slider/',slider),
    path('dashboard/',dashboard),



    path('admin/', admin.site.urls),
]
