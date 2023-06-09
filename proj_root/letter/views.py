from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Letter

# Create your views here.
class index(ListView):
    template_name = 'letter/letter.html'
    model = Letter
    
    
    
