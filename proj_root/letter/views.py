from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Letter
from .forms import LetterForm
# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'

class LetterView(ListView):
    template_name = 'letter/letter.html'
    model = Letter
    
class CreateLetterView(CreateView):
    template_name = 'letter/create_letter.html'
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('letter')

class UpdateLetterView(UpdateView):
    template_name = 'letter/update_letter.html'
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('letter')
    
class DeleteLetterView(DeleteView):
    template_name = 'letter/delete_letter.html'
    model = Letter
    success_url = reverse_lazy('letter')
    

class LetterContentView(DetailView):
    template_name = 'letter/letter_content.html'
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letter_content'] = Letter.content
        return context
    
    
        
        
    
    
    
    
