from django.urls import path
from .views import *


urlpatterns = [    
    path('differentiation/', differentiation_api),               # Abbosjon  
    path('taylor-series/', taylors_method_api),                  # Elnazar   
    path('newtons-method/', newtons_method_api),                 # Abbosjon  
    path('simpsons-method/', simpsons_method_api),               # Elnazar   
    path('trapezoid-method/', trapezoid_method_api),             # Ilkhom    
    path('rectangle-method/', rectangle_method_api),             # Eldar      
    path('definite-integral/', definite_integral_api),           # Ilkhom         
    path('indefinite-integral/', indefinite_integral_api),       # Aizada    
    path('limit-calculator/', limit_api),                        # Eldar
]
