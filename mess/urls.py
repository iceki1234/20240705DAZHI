from django.urls import path
from . import views

urlpatterns = [

    path('',views.MessList.as_view(), name='mess_list'),

    path('<int:pk>/', views.MessRead.as_view(), name='mess_view'),

    path('create/', views.MessNew.as_view(), name='mess_create')
]