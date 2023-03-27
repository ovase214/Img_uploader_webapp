# from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,ListView

from .models import Post
from .forms import *
# import generic UpdateView
from django.views.generic.edit import DeleteView
 



class HomePageView(TemplateView):
    model=Post
    template_name='home.html'

class Home1View(LoginRequiredMixin, ListView):
    model=Post
    template_name='Img_list.html'
    login_url = reverse_lazy('home')


class CreatePostView(LoginRequiredMixin, CreateView):
    model=Post
    form_class=PostForm
    template_name='dashboard.html'
    success_url = reverse_lazy('Img_list')
    

class SignUpView(CreateView):
    model=Post
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'



class DeleteImg(DeleteView):
    # specify the model you want to use
    model = Post   
    
    # url to redirect after successfully    
    success_url ="/Img_list"
     
    template_name = "Delete.html"