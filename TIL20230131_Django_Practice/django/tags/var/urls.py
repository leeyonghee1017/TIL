from django.urls import path, include
from . import views

app_name='var'
urlpatterns = [    
    path('',views.index),    
    path('var01/',views.variable01),    
    path('var02/',views.variable02), 
    path('for/',views.testfor),  
    path('if01',views.if01),
    path('if02',views.if02),
]