from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView, 
    UpdateView
    )
from apps.account.forms import (
    UserRegisterForm, 
    UserProfileForm
    )
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm
    )
from django.views.generic.base import (
    View
    )



class LoginView(LoginView):
    '''
    this view use the default django login view
    '''
    template_name = 'account/login.html'


class SignUpView(CreateView):
    '''
    this view is for signup
    '''
    form_class = UserRegisterForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')


class UserProfile(LoginRequiredMixin, View):
    '''
    this view displays user information and
    user can update it
    '''
    form_class = UserProfileForm
    

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, 'account/profile.html', context={'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            user = get_user_model().objects.get(username=request.user)
            user.is_complete = True
            user.save()
            return self.get(request, *args, **kwargs)
        
        form_errors = form.errors
        form = self.form_class(instance=request.user)
        context = {
            'form':form,
            'form_errors':form_errors
        }
    
        return render(request, 'account/profile.html', context)

