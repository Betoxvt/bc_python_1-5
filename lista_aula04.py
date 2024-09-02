# Exercícios de Listas e Dicionários resolvidos
# Resoluções de Listas e Dicionários

# # 1. Lista de números ao quadrado

# numeros = list(range(1, 11))

# numeros_quadrados = [x**2 for x in numeros]
# print(numeros_quadrados)

# # 2. Modificar lista de linguagens

# linguagens = ["Python", "Java", "C++", "JavaScript"]

# linguagens_modificada = [x for x in linguagens if x not in 'Java JavaScript']
# print(linguagens_modificada)
# linguagens_modificada.append('R'), linguagens_modificada.append('Ruby')
# print(linguagens_modificada)
# linguagens_modificada.remove('C++')
# print(linguagens_modificada)
# linguagens_modificada.pop()
# print(linguagens_modificada)

# # 3. Informações de um livro

# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
# for k, v in livro.items():
#     print(f'{k.capitalize()}:\t{v}')

# # 4. Contar ocorrências de caracteres, definir a função

# def contar_caracteres(string):
#     contagem = {}
#     for caractere in string:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem


# print(contar_caracteres("Esta é a frase para contar os caracteres"))

# =======================================================================

# def contar_(fonte, argumento) -> int:
#     """
#     -> Conta quantas vezes um argumento está presente em uma fonte
#     :elemento: Any (str, int, bool, float, list, dict...)
#     :caracter: Any (str, int, bool, float, list, dict...)
#     :return: int, número de ocorrências
#     """
#     contagem_do_argumento = str(fonte).count(str(argumento))
#     return contagem_do_argumento


# print(contar_([{'Disponibilidade': True, 'Nome': 'Perdido', 'Custo': 3235}, {'Disponibilidade': True, 'Nome': 'Nunca', 'Custo': 3235}], {'Disponibilidade': True, 'Nome': 'Nunca', 'Custo': 3235}))

# # 5. Preço total da lista de compras

# lista_compras = ["maçã", "banana", "cereja", "maçã", "banana"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65, "laranja": 0.35}

# total = sum(precos[item] for item in lista_compras)
# print(f"Preço total: {total}")

# =============================================================================================================================

# preco_total = 0
# for item_lista in lista_compras:
#     for item, preco in precos.items():
#         if item == item_lista:
#             preco_total += preco
# print(preco_total)

# # Exercícios intermediários e mais avançados

# # 6. Eliminação de Duplicatas
# # Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com", "user@example.com"]

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))

# print(emails_unicos)

# ===================================================================================================

# for email in emails:
#     if emails.count(email) > 1:
#         emails.remove(email)
# print(emails)

# # 7. Filtragem de Dados
# # Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades = [22, 15, 30, 17, 18]

# maiores_18 = [idade for idade in idades if idade >= 18]
# print(maiores_18)

# # 8. Ordenação Personalizada
# # Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Zilcar", "idade": 35},
#     {"nome": "Carol", "idade": 20},
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Joline", "idade": 40}
# ]

# pessoas.sort(key=lambda pessoa: pessoa["nome"])
# print(pessoas)

# # 9. Agregação de Dados
# # Objetivo: Dado um conjunto de números, calcular a média.

# numeros = [10, 20, 30, 40, 50]

# media = sum(numeros) / len(numeros)
# print(media)

# # 10. Divisão de Dados em Grupos
# # Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = [v for v in valores if v%2 == 0]
# impares = [v for v in valores if v%2 != 0]

# =======================================================================================================

# pares = []
# impares = []
# for v in valores:
#     if v%2 == 0:
#         pares.append(v)
#     else:
#         impares.append(v)

# print(impares)
# print(pares)

# # Exercícios com Dicionários
# # 11. Atualização de Dados

# # Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# # # Atualizar o preço do produto com id 2 para 90

# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90

# print(produtos)
        
# # 12. Fusão de Dicionários
# # Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

# dicionario_fusao = {1: dicionario1, 2: dicionario2}
# print(dicionario_fusao)

# # 13. Filtragem de Dados em Dicionário
# # Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

# print(estoque_positivo)

# ========================================================================================================

# produtos_disponiveis = {}
# for produto, quantidade in estoque.items():
#     if quantidade > 0:
#         produtos_disponiveis.update({produto: quantidade})
# print(produtos_disponiveis)

# # 14. Extração de Chaves e Valores
# # Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# dicionario = {"a": 1, "b": 2, "c": 3}

# chaves = [k for k in dicionario.keys()]
# valores = [v for v in dicionario.values()]
# print(chaves)
# print(valores)


# # 15. Contagem de Frequência de Itens
# # Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# texto = "engenharia de dados"
# frequencia = {}

# for caractere in texto:
#     if caractere in frequencia:
#         frequencia[caractere] += 1
#     else:
#         frequencia[caractere] = 1

# print(frequencia)

# ==============================================================

# for c in texto:
#     frequencia.update({c: texto.count(c)})

# print(frequencia)