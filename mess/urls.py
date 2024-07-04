from django.urls import path
from . import views

urlpatterns[

    path('',views.MessList.as_view(), name='mess_list')
]