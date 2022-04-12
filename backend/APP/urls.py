from django.urls import path
from .views import *

urlpatterns = [    
    path('diff/', diff_list),
    path('newton/', newton_list),

]
