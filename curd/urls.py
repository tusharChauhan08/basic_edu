from django.urls import path
from .views import *

urlpatterns = [
    path('home', addData),
    path('update/<int:id>', updateData),
    path('delete/<int:id>', deleteData)
]