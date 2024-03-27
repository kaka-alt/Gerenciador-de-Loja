from django.shortcuts import render
from django.http import HttpResponse

def tela_login(request):
    return render(request, 'tela_login.html')

def tela_cadastro(request):
    return render(request, 'tela_cadastro.html')