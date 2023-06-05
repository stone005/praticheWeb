from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView,ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Pratica, Agente, Magistrato, Indagato
from .forms import PraticaForm
from .choices import *


class PraticaCreateView(CreateView):
	model = Pratica
	form_class = PraticaForm
	success_url = reverse_lazy('pratiche:pratica-list')


class AgenteCreateView(CreateView):
	model = Agente
	template_name = 'pratiche/agente_form.html'
	fields = ('__all__')
	success_url = reverse_lazy('pratiche:agente-list')


class MagistratoCreateView(CreateView):
	model = Magistrato
	fields = ('__all__')
	success_url = reverse_lazy('pratiche:pratica-list')


class IndagatoCreateView(CreateView):
	model = Indagato
	fields = ('__all__')
	success_url = reverse_lazy('pratiche:indagato-list')	
 
 
def load_prot(request):
	tipologia = request.GET['tipologia']
	pratica = Pratica.objects.filter(tipologia=tipologia)
	if not pratica:
		max_prot = 1
	else:
		max_prot = Pratica.objects.values('prot').filter(tipologia=tipologia).order_by('-id')[0]['prot']
		max_prot = max_prot + 1
	return render(request, 'pratiche/new_max_prot.html', {'max_prot':max_prot})


def pratica_list_view(request):
	if request.method == 'POST':
		agente = request.POST.get('cboAgent')
		tipo = request.POST.get('cboTipo')
		if not agente and not tipo:	#Ok senza nessun parametro
			object_list = Pratica.objects.all()
		elif not agente:	#solo tipologia
			object_list = Pratica.objects.filter(tipologia = tipo)
		elif not tipo:		#solo agente
			if agente == 'all':		#tutti gli agenti
				object_list = Pratica.objects.all()
			else:					#un solo agente
				object_list = Pratica.objects.filter(agente = agente)
		else:				#entrambi i parametri
			if agente == 'all':
				object_list = Pratica.objects.all()
			else:
				object_list = Pratica.objects.filter(tipologia = tipo, agente = agente)
	else:
		object_list = Pratica.objects.all()

	agenti_list = Agente.objects.all()
	tipo_list = tipo_choices

	context = {
		'object_list': object_list,
		'agenti_list': agenti_list,
		'tipo_list': tipo_list
	}
	return render(request, 'pratiche/pratica_list.html', context)


def pratica_detail_view(request, id=id):
	obj = Pratica.objects.get(id=id)
	context = {
		'object': obj
	}
	return render(request, 'pratiche/pratica_detail.html', context)


class AgenteListView(ListView):
	model = Agente
	template_name = 'pratiche/agente_list.html'


class MagistratoListView(ListView):
	model = Magistrato
	template_name = 'pratiche/magistrato_list.html'


def indagato_list_view(request):
	object_list = Indagato.objects.all()
	context = {
		'object_list': object_list,
	}
	return render(request, 'pratiche/indagato_list.html', context)


class pratiche_indagato(ListView):
	model = Pratica
	template_name = 'pratiche/pratiche_indagato.html'

	def get_queryset(self):
		return Pratica.objects.filter(indagati=self.kwargs.get('pk'))


# def pratiche_indagato(request, pk=None):
# 	if pk:
# 		object_list = Pratica.objects.filter(indagati=pk)
# 	else:
# 		object_list = Pratica.objects.all

# 	context = {
# 		'object_list': object_list,
# 	}
# 	return render(request, 'pratiche/pratiche_indagato.html', context)

class pratiche_agente(ListView):
	model = Pratica
	template_name = 'pratiche/pratiche_indagato.html'

	def get_queryset(self):
		return Pratica.objects.filter(agente=self.kwargs.get('id'))


class pratiche_magistrato(ListView):
	model = Pratica
	template_name = 'pratiche/pratiche_indagato.html'

	def get_queryset(self):
		return Pratica.objects.filter(magistrato=self.kwargs.get('id'))


class PraticaDetailView(DetailView):
	template_name = 'pratiche/pratica_detail.html'

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Pratica, id=id_)


class SignUp(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'