from django.shortcuts import render
from django.views.generic import ListView
from .models import Mess

# Create your views here.
class MessList(ListView):
    model = Mess

    #應用程式/資料模型_list.html
    #mess/mess_list.html