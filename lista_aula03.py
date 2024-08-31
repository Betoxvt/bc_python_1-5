### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# vendas_validas = []
# vendas_invalidas = []
# id_venda = 0
# while True:
#     try:
#         id_venda += 1
#         q = float(input('Quantidade: ').strip().replace(',', '.'))
#         p = float(input('Preço: ').strip().replace(',', '.'))
#         venda = {'ID': id_venda, 'Quantidade': q, 'Preço': p}
#         if q < 0 or p < 0:
#             print('Dados inválidos (negativos)')
#             vendas_invalidas.append(venda)
#         else:
#             print('Dados válidos')
#             vendas_validas.append(venda)
#         while True:
#             c = input('Continuar? [S/N] ').strip().upper()[0]
#             if c in 'SN':
#                 break
#             else:
#                 print('Apenas sim [S] ou não [N]')
#         if c == 'N':
#             print('Finalizando')
#             break
#         elif c == 'S':
#             print('Insira os dados da proxima venda')
#     except ValueError:
#         print('Os dados devem ser numéricos')
#     except KeyboardInterrupt:
#         print('\nPrograma interrompido')
#         break
# print('Vendas válidas', vendas_validas)
# print('Vendas inválidas', vendas_invalidas)

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que: faltou aqui informação mas... 
# Baixa se menor que 60; Normal entre 60 e 90, Alta se maior que 90.

# t = float(input('Sensor Temperatura (ºC): '))
# if t < 60:
#     print('Temperatura baixa')
# elif t > 90:
#     print('Temperatura alta')
# else:
#     print('Temperatura normal')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log1 = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# log2 = {'timestamp': '2021-06-24 10:00:00', 'level': 'CONNECTION', 'message': 'Conected to 192.168.0.32'}
# log3 = {'timestamp': '2021-06-25 10:00:00', 'level': 'ERROR', 'message': 'Acesso negado'}
# log = [log1, log2, log3]
# for l in log:
#     if l['level'] == 'ERROR':
#         print(l['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# import re

# def validar_email_regex(email):
#     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     return re.fullmatch(regex, email)

# joana = {'nome': 'Joana', 'email': 'joana2003@gmail.com', 'idade': 21}
# chico = {'nome': 'Chico', 'email': 'chico.gmail.com', 'idade': 32}
# manu = {'nome': 'Manu', 'email': 'manu222@gmail', 'idade': 18}
# maria = {'nome': 'Maria', 'email': 'mariazinha@hotmail.com', 'idade': 16}
# simone = {'nome': 'Simone', 'email': 'simone@hotmail.com', 'idade': 70}
# sonia = {'nome': 'Sonia', 'email': 'SOnia@hotmail.com', 'idade': 66}

# users = [joana, chico, manu, maria, simone, sonia]

# for u in users:
#     if not 18 <= u['idade'] <= 65:
#         print(f'Usuário {u['nome']} com idade fora dos limites')
#     elif not validar_email_regex(u['email']):
#         print(f'Usuário {u["nome"]} com e-mail inválido')
#     else:
#         print(f'Usuário {u["nome"]} válido')

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 2000, 'hora': 20}
# if transacao['valor'] > 10000:
#     print('Transação suspeita, valor acima de R$10.000,00')
# elif 18 < transacao['hora'] > 9:
#     print('Transação suspeita, horário entre 18h e 9h')
# else:
#     print('Transação normal')

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# txt = 'Um texto comum, outro texto comum, nada incomum'
# palavras = txt.strip().replace(',','').split()
# contagem = dict()
# for p in palavras:
#     if p not in contagem:
#         contagem[p] = 1
#     else:
#         contagem[p] += 1
# print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# # normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
# normalizados = []
# for n in numeros:
#     normalizados.append((n - minimo) / (maximo - minimo))
# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)

# dados = [
#     {'nome': 'Manu', 'idade': 32, 'saldo': 3200},
#     {'nome': 'Natalia', 'idade': 35, 'saldo': 12200},
#     {'nome': 'Pedro', 'idade': 25, 'saldo': ''},
#     {'nome': 'Fabi', 'idade': '', 'saldo': ''}
# ]

# invalid_users = []
# for user in dados:
#     for k, v in user.items():
#         if not v and user['nome'] not in invalid_users:
#             invalid_users.append(user['nome'])
# print('Usuários com cadastro inválido: ', end='')
# for nome in invalid_users:
#     print(nome, end= '; ')
# print()

# valid_users = []
# for user in dados:
#     if user['nome'] not in invalid_users:
#         valid_users.append(user['nome'])
# print('Usuários com cadastro válido: ', end='')
# for nome in valid_users:
#     print(nome, end='; ')
# print()

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1, 11)
# pares = [x for x in numeros if x % 2 == 0]
# print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "eletrônicos", "valor": 200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "livros", "valor": 100},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)

### tinha dado errado antes e tentei assim também
# total = []
# total2 = {}
# for venda in vendas:
#     for v in venda.values():
#         total.append(v)
# for i, j in enumerate(total):
#     if i % 2 == 0 and j not in total2:
#         total2[j] = total[i+1]
#     elif i % 2 == 0 and j in total2:
#         total2[j] += total[i+1]
# print(total2)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.