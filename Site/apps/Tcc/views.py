from . import forms, models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'arqtcc/home.html')
  

def adicionar(request):
    if request.method == "POST":
        form = forms.tccform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("visualizar"))

    else:
        form = forms.tccform()
    return render(request, 'arqtcc/inserirtcc.html', {'form':form})


def visualizar(request):
    dadosform = models.Tcc.objects.all()
    return render(request, 'arqtcc/visualizartcc.html', {'tasks':dadosform})

def editar(request, id):
    task = get_object_or_404(models.Tcc, pk=id)
    form = forms.tccform(instance=task)
    if request.method == 'POST':
        form = forms.tccform(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return HttpResponseRedirect(reverse_lazy("visualizar"))
        else:
            return render(request, 'arqtcc/editartcc.html', {'form':form, 'task':task})
    else:
       return render(request, 'arqtcc/editartcc.html', {'form':form, 'task':task})

def deletar(request,id):
    task = get_object_or_404(models.Tcc, pk=id)
    task.delete()
    return HttpResponseRedirect(reverse_lazy("visualizar"))
