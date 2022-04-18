from django.urls import path
from .views import *

urlpatterns = [    
    path('diff/', diff_list),                      #Abbosjon
    path('taylor/', taylor_list),                  #Elnazar
    path('newton/', newton_list),                  #Abbosjon
    path('simpson/', simpson_list),                #Elnazar
    path('trapezoid/', trapezoid_list),            #Ilkhom
]
