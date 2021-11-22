from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .programa import return_graph, graph_horario, grafico_log, log_horario
from .forms import BairroForm, LogradourosForm


def index(request):
	template=loader.get_template('bairros/index.html')
	context={}
	return HttpResponse(template.render(context,request))

def sobre_nos(request):
	template=loader.get_template('bairros/sobre_nos.html')
	context={}
	return HttpResponse(template.render(context,request))

'''def pesquisar_por_bairro(request):
	template=loader.get_template('bairros/por_bairro.html')
	context={}
	context['graph1']=return_graph()
	context['graph2']=graph_horario()
	return HttpResponse(template.render(context, request))'''

'''def pesquisar_por_logradouro(request):
	template=loader.get_template('bairros/por_logradouro.html')
	context={}
	context['grafRFlog']=grafico_log()
	context['logHorario']=log_horario()
	return HttpResponse(template.render(context, request))'''

def pesquisar_por_bairro(request):
	# se for um POST, é pq a pessoa submeteu o formulário
	if request.method == 'POST':
		# Cria o formulário a partir do que você recebeu
		form = BairroForm(request.POST)
		# Verifica se é valido
		if form.is_valid():
			bairro_selecionado = form.cleaned_data['bairro']
			#bairro_selecionado = form.label
			# Busca os dados do bairro
			# (teria que buscar no banco)
			dados = return_graph(bairro_selecionado)
			dados1=graph_horario(bairro_selecionado)
			#res = list(bairro_selecionado.values())[0]
			
			#dados=return_graph(res)


			# Manda pra mesma url, mas agora com os dados:
			# vc pode mandar pra outra tb
			return render(request, 'bairros/por_bairro.html', {'dados': dados, 'dados1':dados1, 'form': form})

	# Se for um get, cria um form novo
	else:
		form = BairroForm()
		#template=loader.get_template('bairros/por_bairro.html')
		#if form.is_valid():			
		#bairro_selecionado = form.cleaned_data['bairro']
		#dados= f"asdfasd {bairro_selecionado}"
		#return HttpResponse(template.render({'dados': dados,'form': form}, request))
		return render(request, 'bairros/por_bairro.html', {'form': form})


def pesquisar_por_logradouro(request):
	# se for um POST, é pq a pessoa submeteu o formulário
	if request.method == 'POST':
		# Cria o formulário a partir do que você recebeu
		form = LogradourosForm(request.POST)
		# Verifica se é valido
		if form.is_valid():
			logradouro_selecionado = form.cleaned_data['logradouro']
			# Busca os dados do bairro
			# (teria que buscar no banco)
			dados = grafico_log(logradouro_selecionado)
			dados1=log_horario(logradouro_selecionado)

			# Manda pra mesma url, mas agora com os dados:
			# vc pode mandar pra outra tb
			return render(request, 'bairros/por_logradouro.html', {'dados': dados, 'dados1':dados1,'form': form})

	# Se for um get, cria um form novo
	else:
		form = LogradourosForm()
		return render(request, 'bairros/por_logradouro.html', {'form': form})


