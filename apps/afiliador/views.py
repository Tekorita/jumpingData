from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.afiliador.forms import AfiliadorForm
from apps.afiliador.models import Afiliador


# Create your views here.

#def index(request):
#	return HttpResponse("Index de mascota")


#-----------------------------------VISTAS BASADAS EN FUNCIONES-------------------------------------------

def index(request):
	return render(request, 'index.html')

def afiliador_view(request):
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = AfiliadorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('afiliador_listar')
	else:
		form = AfiliadorForm()

	return render(request, 'afiliador/afiliador_form.html', {'form':form})

def afiliador_list(request):
	# import pdb; pdb.set_trace()
	afiliador = Afiliador.objects.all().order_by('id_afiliador')
	# import pdb; pdb.set_trace()
	contexto = {'afiliadores':afiliador}
	import pdb; pdb.set_trace()
	return render(request, 'afiliador/afiliador_list.html', contexto)


def afiliador_edit(request, id_afiliador):
	afiliador = Afiliador.objects.get(id=id_afiliador)
	if request.method == 'GET':
		form = AfiliadorForm(instance=afiliador)
	else:
		form = AfiliadorForm(request.POST, instance=afiliador)
		if form.is_valid():
			form.save()
		return redirect('afiliador_listar')
	return render(request, 'afiliador/Afiliador_form.html', {'form':form})

def afiliador_delete(request, id_afiliador):
	afiliador = Afiliador.objects.get(id=id_afiliador)
	if request.method == 'POST':
		afiliador.delete()
		return redirect('afiliador_listar')
	return render(request, 'afiliador/Afiliador_delete.html', {'afiliador':afiliador})

class AfiliadorList(ListView):
	model = Afiliador
	template_name = 'afiliador/afiliador_list.html'
	paginate_by = 8
