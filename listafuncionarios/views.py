from django.shortcuts import render
from .models import Funcionario
from django.views.decorators.csrf import csrf_protect

def listagem(request):
    titulo = 'Listagem de Funcionarios'
    funcionarios = Funcionario.objects.all()
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':funcionarios})

def selecao(request, id):
    titulo = 'Listagem de Funcionarios'
    funcionario = Funcionario.objects.get(id=id)
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':[funcionario]})

@csrf_protect
def consulta(request):
    consulta = request.POST.get('consulta')
    campo = request.POST.get('campo')
    
    if campo == 'nome':
        funcionarios = Funcionario.objects.filter(nome__contains=consulta)
    elif campo == 'idade':
        funcionarios = Funcionario.objects.filter(idade__contains=consulta)
    elif campo == 'sexo':
        funcionarios = Funcionario.objects.filter(sexo__contains=consulta)
    elif campo == 'salario':
        funcionarios = Funcionario.objects.filter(salario__contains=consulta)

    titulo = 'Listagem de Pessoas'

    return render(request, 'listagem.html', {'titulo':titulo, 'funcionarios': funcionarios})

_campo = ''
def ordenacao(request, campo):
    titulo = 'Listagem de Funcionarios'
    global _campo
    if campo == _campo:
        funcionarios = Funcionario.objects.all().order_by(campo).reverse()
        _campo = ''
    else:
        funcionarios = Funcionario.objects.all().order_by(campo)
        _campo = campo

    return render(request, 'listagem.html', {'titulo':titulo, 'funcionarios': funcionarios})

def insercao(request):
    titulo = 'Inserir Funcionarios'
    return render(request, 'insercao.html', {'titulo':titulo})

@csrf_protect
def salvar_insercao(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    sexo = request.POST.get('sexo')
    salario = request.POST.get('salario')
    salario = salario.replace(',','.')

    objeto = Funcionario(
        nome=nome,
        idade=idade,
        sexo=sexo,
        salario=salario
    )
    objeto.save
    
    titulo = 'Listagem de Funcionarios'
    funcionarios = Funcionario.objects.all()
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':funcionarios})



def edicao(request):
    titulo = 'Edição de Funcionarios'
    funcionario = Funcionarios.objects.all()
    return render(request,'edicao.html', {'titulo':titulo, 'funcionario':funcionario})

@csrf_protect
def salvar_edicao(request):
    id = request.POST.get('id')
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    sexo = request.POST.get('sexo')
    salario = request.POST.get('salario')
    salario = salario.replace(',','.')

    Funcionario.objects.filter(id=id).update(
        nome=nome,
        idade=idade,
        sexo=sexo,
        salario=salario
    )
    
    titulo = 'Listagem de Funcionarios'
    funcionarios = Funcionario.objects.all()
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':funcionarios})


def delecao(request, id):
    titulo = 'Excluir Funcionario'
    funcionario = Funcionario.objects.get(id=id)
    return render(request,'edicao.html', {'titulo':titulo, 'funcionario':funcionario})

@csrf_protect
def salvar_delecao(request):
    id = request.POST.get('id')

    Funcionario.objects.filter(id=id).delete()
    
    titulo = 'Listagem de Funcionarios'
    funcionarios = Funcionario.objects.all()
    return render(request, 'listagem.html',{'titulo': titulo , 'funcionarios':funcionarios})

def graficos(request):
    titulo = 'Grafico por sexo'
    funcionariosM = Funcionario.objects.filter(sexo='M')
    funcionariosF = Funcionario.objects.filter(sexo='F')

    salarioM = 0
    for m in funcionariosM:
        salarioM += m.salario
    if len(funcionariosM)>0:
       salarioM = salarioM/len(funcionariosM)

    salarioF = 0
    for f in funcionariosF:
        salarioF += f.salario
    if len(funcionariosF)>0:
        salarioF = salarioF/len(funcionariosF)

    idadeM = 0
    for m in funcionariosM:
        idadeM += m.idade
    if len(funcionariosM)>0:
       idadeM = idadeM / len(funcionariosM)
 
    idadeF = 0
    for f in funcionariosF:
        idadeF += f.idade
    if len(funcionariosM)>0:
       idadeF = idadeF / len(funcionariosF)

    return render(request,'graficos.html', {'titulo':titulo, 'salarioM':salarioM,
                                                'salarioF':salarioF, 'idadeM':idadeM, 'idadeF':idadeF})
