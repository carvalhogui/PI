from django import forms

class BairroForm(forms.Form):
	# Aqui você busca todos os bairros disponíveis
	# Botei como exemplo alguns dados, o certo seria pegar no banco
	# O primeiro element é o "ID" e o segundo é a label
	todos_bairros = (
				('1', 'CAPÃO REDONDO'),
				('2', 'MORUMBI'),
				)
	# E você fala pro formulário que tem um campo bairros que aceita qualquer um dos bairros acima
	bairro = forms.ChoiceField(label='Bairro', choices=todos_bairros)