from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Letter, LetterUser, Friends
from .forms import LetterForm, LetterUserForm, FriendsForm
# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'

class LetterView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'letter/letter.html'
    model = Letter


class CreateLetterView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'letter/create_letter.html'
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('letter')

class UpdateLetterView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'letter/update_letter.html'
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('letter')
    
class DeleteLetterView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'letter/delete_letter.html'
    model = Letter
    success_url = reverse_lazy('letter')
    

class LetterContentView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    template_name = 'letter/letter_content.html'
    model = Letter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letter_content'] = Letter.content
        return context
    
    
class LetterUserView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'letter/letter_user.html'
    model = LetterUser
    paginate_by = 3

    
class CreateLetterUser(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'letter/create_letter_user.html'
    model = LetterUser
    form_class = LetterUserForm
    success_url = reverse_lazy('letter_user')
    
    
class Register(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

class FriendView(ListView):
    template_name = 'letter/friend_list.html'
    form_class = FriendsForm
    model = Friends
    
    
        
        
    
    
    
    
