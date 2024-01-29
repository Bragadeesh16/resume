from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.defaultcv,name='defaultcv'),
    path('resume',views.resume,name='resume'),
    path('edit',views.replace,name='edit')
]