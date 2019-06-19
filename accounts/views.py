from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home')
    else :
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})