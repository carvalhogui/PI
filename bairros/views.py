from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .programa import return_graph, graph_horario, grafico_log, log_horario
from .forms import BairroForm, LogradourosForm


def index(request):
	template=loader.get_template('bairros/index.html')
	context={}
	return HttpResponse(template.render(context,request))

# Para a página sobre_nós
def sobre_nos(request):
	template=loader.get_template('bairros/sobre_nos.html')
	context={}
	return HttpResponse(template.render(context,request))


# Utilizando o request método POST, para receber informações solicitadas pelo usuário
def pesquisar_por_bairro(request):
	# se for um POST, é pq a pessoa submeteu o formulário
	if request.method == 'POST':
		# Cria o formulário a partir do que é recebido
		form = BairroForm(request.POST)
		# Verifica se é valido
		if form.is_valid():
			bairro_selecionado = form.cleaned_data['bairro']
			#bairro_selecionado = form.label
			#busca os dados do bairro
			dados = return_graph(bairro_selecionado)
			dados1=graph_horario(bairro_selecionado)
			
			return render(request, 'bairros/por_bairro.html', {'dados': dados, 'dados1':dados1, 'form': form})

	
	else:
		form = BairroForm()
		return render(request, 'bairros/por_bairro.html', {'form': form})


def pesquisar_por_logradouro(request):
	if request.method == 'POST':
		form = LogradourosForm(request.POST)
		if form.is_valid():
			logradouro_selecionado = form.cleaned_data['logradouro']
			dados = grafico_log(logradouro_selecionado)
			dados1=log_horario(logradouro_selecionado)
			return render(request, 'bairros/por_logradouro.html', {'dados': dados, 'dados1':dados1,'form': form})

	else:
		form = LogradourosForm()
		return render(request, 'bairros/por_logradouro.html', {'form': form})


