from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas

def tarefa_listar(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/tarefas_listar.html', {'tarefas': tarefas})

def tarefa_criar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Tarefas.objects.create(nome=nome)
        return redirect('tarefa_listar')
    return render(request, 'tarefas/tarefas_criar.html')

def tarefa_editar(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)
    if request.method == 'POST':
        tarefa.nome = request.POST.get('nome')
        tarefa.pronta = 'pronta' in request.POST
        tarefa.save()
        return redirect('tarefa_listar')
    return render(request, 'tarefas/tarefa_editar.html', {'tarefa': tarefa})

def tarefa_deletar(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefa_listar')
    return render(request, 'tarefas/tarefa_deletar.html', {'tarefa': tarefa})