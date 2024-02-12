from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from accounts.forms import LoginForm, RegistrationForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Profile
from .forms import ProfileForm
# Create your views here.

class RegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = '/accounts/login/'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')



def profile_view(request, pk=None):
    template_name = 'accounts/profile.html'
    profile = None

    if pk is not None:
        # Retrieve an existing profile
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            pass

    user = request.user
    if Profile.objects.filter(user=user).exists():
        # Profile already exists, update the existing profile
        profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile, user=user)

    return render(request, template_name, {'form': form, 'profile': profile})


def profile_delete(request, pk):
    profile = Profile.objects.get(pk=pk)
    print(profile)
    # print("Deleting profile...",profile)
    # if request.method == 'POST':
    #     profile.delete()
    #     print("hi")
    #     return('profle' pk)
