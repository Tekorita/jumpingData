from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.sede.forms import SedeForm
from apps.sede.models import Sede


# Create your views here.

#def index(request):
#	return HttpResponse("Index de mascota")


#-----------------------------------VISTAS BASADAS EN FUNCIONES-------------------------------------------

def index(request):
	return render(request, 'index.html')

def sede_view(request):
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = SedeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('sede_listar')
	else:
		form = SedeForm()

	return render(request, 'sede/sede_form.html', {'form':form})

def sede_list(request):
	# import pdb; pdb.set_trace()
	sede = Sede.objects.all().order_by('id')
	# import pdb; pdb.set_trace()
	contexto = {'sedes':sede}
	import pdb; pdb.set_trace()
	return render(request, 'sede/sede_list.html', contexto)


def sede_edit(request, id_sede):
	sede = Sede.objects.get(id=id_sede)
	if request.method == 'GET':
		form = SedeForm(instance=sede)
	else:
		form = SedeForm(request.POST, instance=sede)
		if form.is_valid():
			form.save()
		return redirect('sede_listar')
	return render(request, 'sede/sede_form.html', {'form':form})

def sede_delete(request, id_sede):
	sede = Sede.objects.get(id=id_sede)
	if request.method == 'POST':
		sede.delete()
		return redirect('sede_listar')
	return render(request, 'sede/Sede_delete.html', {'sede':sede})

class SedeList(ListView):
	model = Sede
	template_name = 'sede/sede_list.html'
	paginate_by = 8
