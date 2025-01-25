from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def authenticate_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    else:
        return render(request, 'accounts/login.html', {})

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('contacts:create'))
    else:
        return render(request, "accounts/login.html", {"message": "Usuário ou senha inválidos."})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))
