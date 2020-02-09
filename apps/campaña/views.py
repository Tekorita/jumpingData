from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.campaña.forms import CampañaForm
from apps.campaña.models import Campaña


# Create your views here.

#def index(request):
#	return HttpResponse("Index de mascota")


#-----------------------------------VISTAS BASADAS EN FUNCIONES-------------------------------------------

def index(request):
	return render(request, 'campaña/index.html')

def campaña_view(request):
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = CampañaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('campaña_listar')
	else:
		form = CampañaForm()

	return render(request, 'campaña/campaña_form.html', {'form':form})

def campaña_list(request):
	# import pdb; pdb.set_trace()
	campaña = Campaña.objects.all().order_by('id')
	# import pdb; pdb.set_trace()
	contexto = {'campañas':campaña}
	import pdb; pdb.set_trace()
	return render(request, 'campaña/campaña_list.html', contexto)


def campaña_edit(request, id_campaña):
	campaña = Campaña.objects.get(id=id_campaña)
	if request.method == 'GET':
		form = CampañaForm(instance=campaña)
	else:
		form = CampañaForm(request.POST, instance=campaña)
		if form.is_valid():
			form.save()
		return redirect('campaña_listar')
	return render(request, 'campaña/campaña_form.html', {'form':form})

def campaña_delete(request, id_campaña):
	campaña = Campaña.objects.get(id=id_campaña)
	if request.method == 'POST':
		campaña.delete()
		return redirect('campaña_listar')
	return render(request, 'campaña/campaña_delete.html', {'campaña':campaña})

class CampañaList(ListView):
	model = Campaña
	template_name = 'campaña/campaña_list.html'
	paginate_by = 8
