from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamento.forms import DepartamentoForm
from apps.departamento.models import Departamento


# Create your views here.

#def index(request):
#	return HttpResponse("Index de mascota")


#-----------------------------------VISTAS BASADAS EN FUNCIONES-------------------------------------------

def index(request):
	return render(request, 'index.html')

def departamento_view(request):
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = DepartamentoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('departamento_listar')
	else:
		form = DepartamentoForm()

	return render(request, 'departamento/departamento_form.html', {'form':form})

def departamento_list(request):
	# import pdb; pdb.set_trace()
	departamento = Departamento.objects.all().order_by('id')
	# import pdb; pdb.set_trace()
	contexto = {'departamentos':departamento}
	import pdb; pdb.set_trace()
	return render(request, 'departamento/departamento_list.html', contexto)


def departamento_edit(request, id_departamento):
	departamento = Departamento.objects.get(id=id_departamento)
	if request.method == 'GET':
		form = DepartamentoForm(instance=departamento)
	else:
		form = DepartamentoForm(request.POST, instance=departamento)
		if form.is_valid():
			form.save()
		return redirect('departamento_listar')
	return render(request, 'departamento/departamento_form.html', {'form':form})

def departamento_delete(request, id_departamento):
	departamento = Departamento.objects.get(id=id_departamento)
	if request.method == 'POST':
		departamento.delete()
		return redirect('departamento_listar')
	return render(request, 'departamento/departamento_delete.html', {'departamento':departamento})

class DepartamentoList(ListView):
	model = Departamento
	template_name = 'departamento/departamento_list.html'
	paginate_by = 8
