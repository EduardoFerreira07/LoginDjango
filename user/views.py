from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user =  User.objects.filter(username=username).first()

        if user: 
            return HttpResponse("Usuário já existe!")
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse("Usuário Cadastrado!")

    
    
    return render(request, 'cadastro.html')


def login(request):

    if request.method == "POST":
        
        username =  request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse("Autenticado!")
        
        else:
            return HttpResponse("Email ou senha inválido!")


    return render(request, 'login.html')


@login_required(login_url="/auth/login/")
def plataforma(request):
    return HttpResponse("Acesso autorizado a plataforma!")