from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [
    path('',index,name = 'index'),
    path('create/',PostCreate.as_view(),name = 'create'),
    path('detail/<int:pk>/',detail,name = 'detail'),
]