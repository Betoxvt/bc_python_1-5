# Exercícios de Listas e Dicionários resolvidos
# Resoluções de Listas e Dicionários
# 1. Lista de números ao quadrado

numeros = list(range(1, 11))

# 2. Modificar lista de linguagens

linguagens = ["Python", "Java", "C++", "JavaScript"]

# 3. Informações de um livro

livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}


# 4. Contar ocorrências de caracteres

print(contar_caracteres("engenharia de dados"))

# 5. Preço total da lista de compras

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# Exercícios intermediários e mais avançados
# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

numeros = [10, 20, 30, 40, 50]

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercícios com Dicionários
# 11. Atualização de Dados

# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90



# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}
