# Sobre o projeto
Link para o projeto, pelo Heroku - https://estatisticas-capao.herokuapp.com/pagina_inicial/pagina_inicial.

Aplicação feita para a disciplina de Projeto Integrador I, da UNIVESP.

Essa aplicação utiliza os dados dos boletins de ocorrências de roubo e furto de celulares, na região do Capão Redondo. Os dados oficiais estão no portal da Secretaria de Segurança Pública de SP - http://www.ssp.sp.gov.br/transparenciassp/.

Os usuários podem pesquisar por bairros e/ou ruas da região do Capão Redondo, para obterem informações mais detalhadas sobre a quantidade de roubo e furto de celulares e o período do dia das ocorrências. 

As informações contidas no projeto podem não representar a real quantidade de ocorrências, pois, durante o pré-processamento dos dados, foram constatados muitos erros nos boletins de ocorrência. Esses erros durante o preenchimento do boletim de ocorrência compromete a contagem exata das ocorrências nos bairros e/ou ruas. 

# Tecnologias utilizadas
- Python 3
- Django
- SQLite3
- SQLAlchemy
- Jinja
- Bootstrap
- HTML, CSS, JS

# Principais bibliotecas utilizadas (python)
- Selenium (extração automática dos dados)
- Pandas e Numpy (organização e pré-processamento dos dados)
- Difflib (Para minimizar e corrigir nomes incorretos encontrados nos boletins de ocorrência)
- Matplotlib
