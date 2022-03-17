from django.urls import path
from design.views import *


urlpatterns = [
     path('',navigation,name='index'),
     path('signup',Signup,name='signup'),
     path('login',Login,name='login'),
     path('joblist',JobList,name='joblist'),
     path('apply',apply,name='apply'),
     ]


#just to test webhooks
