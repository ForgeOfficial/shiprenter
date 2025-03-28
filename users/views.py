from django.shortcuts import redirect

from .forms.LoginForm import LoginForm
from .forms.RegisterForm import RegisterForm
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'password2': request.POST.get('password2'),
        }
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'auth.html',
                          {'active': 'login', 'login_form': LoginForm(), 'register_form': RegisterForm(data),
                           'success': 'Successfully registered'})
        return render(request, 'auth.html',
                      {'active': 'register', 'login_form': LoginForm(), 'register_form': RegisterForm(data),
                       'error': next(iter(serializer.errors.values()))[0]})
    else:
        return render(request, 'auth.html',
                      {'active': 'register', 'login_form': LoginForm(), 'register_form': RegisterForm()})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password'),
        }
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                response = redirect('profile')
                return response
            return render(request, 'auth.html',
                          {'active': 'login', 'login_form': LoginForm(data), 'register_form': RegisterForm(),
                           'error': 'Username or password is invalid'})
        return render(request, 'auth.html',
                      {'active': 'login', 'login_form': LoginForm(data), 'register_form': RegisterForm(),
                       'error': 'Username or password is invalid'})
    else:
        return render(request, 'auth.html',
                      {'active': 'login', 'login_form': LoginForm(), 'register_form': RegisterForm()})


def logout_view(request):
    logout(request)
    return redirect('login')