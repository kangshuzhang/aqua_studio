"""aqua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from studio import views as studio_views
from django.conf.urls.static import static  
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('home/', studio_views.home,name='home'),
    path('diary/', studio_views.diary,name='diary'),
    path('diary2/', studio_views.diary2,name='diary2'),
    path('diary3/', studio_views.diary3,name='diary3'),
    path('diary4/', studio_views.diary4,name='diary4'),
    path('diary5/', studio_views.diary5,name='diary5'),
    path('diary6/', studio_views.diary6,name='diary6'),
    path('diary7/', studio_views.diary7,name='diary7'),
    path('data/', studio_views.data,name='data'),
    path('data_concentration/', studio_views.data_concentration,name='data_concentration'),
    path('data_concentration2/', studio_views.data_concentration2,name='data_concentration2'),
    path('data_concentration3/', studio_views.data_concentration3,name='data_concentration3'),
    path('data_advance/', studio_views.data_advance,name='data_advance'),
    path('contact/', studio_views.contact,name='contact'),
    path('intelligence/', studio_views.intelligence,name='intelligence'),
    path('intelligence2/', studio_views.intelligence2,name='intelligence2'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
