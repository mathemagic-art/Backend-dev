from django.urls import path
from .views import *


urlpatterns = [    
    path('differentiation/', diff_list),                          #Abbosjon  
    path('taylor-series/', taylor_list),                          #Elnazar   
    path('newtons-method/', newton_list),                         #Abbosjon  
    path('simpsons-method/', simpson_list),                       #Elnazar   
    path('trapezoid-method/', trapezoid_list),                    #Ilkhom    
    path('rectangle-method/', rectangle_list),                    #Eldar      
    path('definite-integral/', definite_integral_list),           #Ilkhom    
    path('limit-calculator/', limit_list),                        #Eldar     
    path('indefinite-integral/', indefinite_integral_list),       #Aizada    

]
