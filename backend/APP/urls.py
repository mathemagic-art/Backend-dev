from django.urls import path
from .views import *

urlpatterns = [
    path('newton/', newton_list),
    path('diff/', diff_list),
]
