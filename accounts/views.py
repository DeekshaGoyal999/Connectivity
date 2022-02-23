from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.conf import settings


User=settings.AUTH_USER_MODEL

# Create your views here.


def login_view(request,*args,**kwargs):
    form=AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user_= form.get_user()
        login(request,user_)
        return redirect("/posts/p/")
    context={"form":form,
    "btn-label":"Login",
    "title":"Login"}
    return render(request, "accounts/auth.html",context)

def register_view(request,*args,**kwargs):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=True)
        username = form.cleaned_data.get('username') 
        messages.success(request, f'Your account has been created!' ) 
        login(request,user)
        return redirect("/posts/p/")
    context={"form":form,
    "btn-label":"Register",
    "title":"Register"}
    return render(request,"accounts/auth.html",context)


def logout_view(request, *args,**kargs):
    if request.method=='POST':
        logout(request)
        return redirect("/accounts/login")
    context={"form":None,
    "btn-label":"Logout",
    "title":"Logout"}
    return render(request,"accounts/auth.html",context)

@login_required
def profile_view(request,*args,**kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("http://127.0.0.1:8000/accounts/profile/") # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)




