from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from .forms import registerForm 

class UserRegisterView(CreateView):
    model = User
    form_class = registerForm
    template_name = 'usuarios/register.html'  
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user:
            login(self.request, user)
        return response
    
class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def get_success_url(self):
        return reverse_lazy('inicio')
    
class CustomlogoutView(LogoutView):
    next_page = reverse_lazy('inicio')


class profileView(DetailView):
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user