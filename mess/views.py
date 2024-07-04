from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Mess

# Create your views here.
class MessList(ListView):
    model = Mess

#應用程式/資料模型_list.html
#mess/mess_list.html
class MessRead(DetailView):
    model = Mess
    
class MessNew(CreateView):
    model = Mess
    fields = ['user', 'receipt', 'subject', 'content']
    success_url = '/mess/'
    