from django.shortcuts import render
from .models import Pessoa

def mostrar_formulario(request):
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST['nome']
        pessoa.cpf = request.POST['cpf']
        pessoa.save()


def mostrar_hello(request):
    return render(request, 'index.html')

def mostrar_pessoas(request):
    pessoas = Pessoa.objects.all()

    return render(request,'pessoas.html', {'dados': pessoas})