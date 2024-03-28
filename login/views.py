from django.shortcuts import render
from django.http import HttpResponse
from .models import register

def tela_login(request):
    return render(request, 'tela_login.html')

def tela_cadastro(request):
     if request.method == 'GET':
        return render(request, 'tela_cadastro.html')
     elif request.method =='POST':
         nome = request.POST.get('nome')
         email = request.POST.get('email')
         

         conta = register(nome=nome, email=email)

         conta.save()
         return HttpResponse ('cadastro com sucesso')
   