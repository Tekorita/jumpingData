from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.distrito.forms import DistritoForm
from apps.distrito.models import Distrito


# Create your views here.

#def index(request):
#	return HttpResponse("Index de mascota")


#-----------------------------------VISTAS BASADAS EN FUNCIONES-------------------------------------------

def index(request):
	return render(request, 'distrito/index.html')

def distrito_view(request):
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = DistritoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('distrito_listar')
	else:
		form = DistritoForm()

	return render(request, 'distrito/distrito_form.html', {'form':form})

def distrito_list(request):
	# import pdb; pdb.set_trace()
	distrito = Distrito.objects.all().order_by('id')
	# import pdb; pdb.set_trace()
	contexto = {'distritos':distrito}
	import pdb; pdb.set_trace()
	return render(request, 'distrito/distrito_list.html', contexto)


def distrito_edit(request, id_distrito):
	distrito = Distrito.objects.get(id=id_distrito)
	if request.method == 'GET':
		form = DistritoForm(instance=distrito)
	else:
		form = DistritoForm(request.POST, instance=distrito)
		if form.is_valid():
			form.save()
		return redirect('distrito_listar')
	return render(request, 'distrito/distrito_form.html', {'form':form})

def distrito_delete(request, id_distrito):
	distrito = Distrito.objects.get(id=id_distrito)
	if request.method == 'POST':
		distrito.delete()
		return redirect('distrito_listar')
	return render(request, 'distrito/distrito_delete.html', {'distrito':distrito})

class DistritoList(ListView):
	model = Distrito
	template_name = 'distrito/distrito_list.html'
	paginate_by = 8
