from django.urls import path
from .views import *

urlpatterns = [    
    path('diff/', diff_list),
    path('taylor/', taylor_list),
    path('newton/', newton_list),
    path('simpson/', simpson_list),
    path('trapezoid/', trapezoid_list),
]
