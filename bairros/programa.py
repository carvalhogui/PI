import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
df=pd.read_sql_query("SELECT * FROM dados",conn)


# PARA OS BAIRROS
def return_graph(bairro_selecionado):
    ano=[2015,2016,2017,2018,2019,2020,2021]
    lista=[]
    for j in range(len(ano)):
        i = df[((df['BAIRRO'] == bairro_selecionado) & (df['year'] == ano[j]))].index
        lista.append(i.shape[0])
    
    fig = plt.figure()
    plt.xlabel("Ano")
    plt.ylabel("Quantidade de ocorrências")
    plt.title(bairro_selecionado+ '- Roubo e Furto de celulares')
    plt.plot(ano,lista)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
    
def graph_horario(bairro_selecionado):
    horarios=['PELA MANHÃ', 'A TARDE', 'A NOITE', 'DE MADRUGADA']
    l_horario=[]
    for k in range(len(horarios)):
        p=df[((df['BAIRRO'] == bairro_selecionado) & (df['PERIDOOCORRENCIA'] == horarios[k]))].index
        l_horario.append(p.shape[0])

    fig_horario = plt.figure()
    plt.xlabel("Período do dia")
    plt.ylabel("Quantidade de ocorrências")
    plt.title(bairro_selecionado+' - Período do dia')
    plt.bar(horarios,l_horario)

    imgdata2 = StringIO()
    fig_horario.savefig(imgdata2, format='svg')
    imgdata2.seek(0)

    data2 = imgdata2.getvalue()
    return data2

# PARA LOGRADOURO
def grafico_log(logradouro_selecionado):
    ano=[2015,2016,2017,2018,2019,2020,2021]
    lista=[]
    for j in range(len(ano)):
        i = df[((df['LOGRADOURO'] == logradouro_selecionado) & (df['year'] == ano[j]))].index
        lista.append(i.shape[0])
    
    fig = plt.figure()
    plt.xlabel("Ano")
    plt.ylabel("Quantidade de ocorrências")
    plt.title(logradouro_selecionado +'- Roubo e Furto de celulares')
    plt.plot(ano,lista)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
    
def log_horario(logradouro_selecionado):
    horarios=['PELA MANHÃ', 'A TARDE', 'A NOITE', 'DE MADRUGADA']
    l_horario=[]
    for k in range(len(horarios)):
        p=df[((df['LOGRADOURO'] == logradouro_selecionado) & (df['PERIDOOCORRENCIA'] == horarios[k]))].index
        l_horario.append(p.shape[0])

    fig_horario = plt.figure()
    plt.xlabel("Período do dia")
    plt.ylabel("Quantidade de ocorrências")
    plt.title(logradouro_selecionado+ ' - Período do dia')
    plt.bar(horarios,l_horario)

    imgdata2 = StringIO()
    fig_horario.savefig(imgdata2, format='svg')
    imgdata2.seek(0)

    data2 = imgdata2.getvalue()
    return data2


'''def return_graph():

    plt.xlabel("Ano")
    plt.ylabel("Quantidade de ocorrências")
    plt.title('PARQUE FERNANDA - Roubo e Furto de celulares')
    teste=plt.plot(ano,lista)
    return teste





    fig = plt.figure()
    
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
'''