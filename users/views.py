from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import AccountAuthenticationForm, RegistrationForm
from .models import User

# Create your views here.


def register_page_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.username}")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("index")
        else:
            context['registration_form'] = form

    return render(request, 'users/register.html', context)


def login_page_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("index")
    context = {}

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)

            if destination:
                return redirect(destination)

            return redirect("index")
        else:
            context['login_form'] = form

    return render(request, 'users/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def logout_view(request):
    logout(request)
    return redirect("index")


def user_page_view(request, *args, **kwargs):
    template = 'users/user_page.html'
    context = {}
    # user_name = kwargs.get("user_name")
    user_id = kwargs.get("user_id")
    try:
        account = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponse("That user doesn't exist")
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['hide_email'] = account.hide_email

        is_self = True
        is_friend = False
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = settings.BASE_URL

    return render(request, template, context)
