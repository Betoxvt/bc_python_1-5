# Escreva um programa em Python que solicita ao usuário que digite seu nome, o valor do seu salário mensal e o valor do bônus que recebeu, O programa deve, então , imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido. + Com tratamento de erros.

# Constante do KPI 2024
CONSTANTE_BONUS = 1000

# Imprime um texto com o solicitado pelo desafio

# 1) Solicita ao usuário que digite seu nome
try:
    nome = str(input("Insira seu nome: ").strip().title())
    if any(char.isdigit() for char in nome):
        print('Nome não deve conter números')
        exit()
    elif not nome:
        print('Nome não deve estar vazio')
        exit()
except Exception as e:
    print(f'Erro, {e}')
    exit()
else:
    print(f'Nome válido registrado: {nome}')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

try:
    salario = float(input("Insira o valor de seu salário mensal: R$").strip().replace(',', '.'))
    if salario < 0:
        print('O salário deve ser um número positivo')
        exit()
except ValueError:
    print('Entrada inválida. O salário deve ser um número')
    exit()
except Exception as e:
    print(f'Erro, {e}')
else:
    print(f'Salário registrado: R${salario:.2f}')

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    bonus = float(input("Insira o bônus (%): ")) / 100
    if bonus < 0:
        print('O bônus deve ser um número positivo')
        exit()
except ValueError:
    print('O bônus deve ser um número')
    exit()
else:
    print(f'Bônus de {bonus*100}% = {bonus}')

# 4) Calcule o valor do bônus final
bonus_final = bonus * salario

# 5) Imprima cálculo do KPI para o usuário
kpi = CONSTANTE_BONUS + bonus_final
print(f'Cálculo do KPI:\nKPI = 1000 + ({salario} X {bonus}) = R${kpi}')

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
novo_salario = salario + kpi
print(f'Saudações {nome}, seu salário agora é de R${novo_salario:.2f}')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Problemas em erros de digitação, como usar vírgula ao invés de ponto para os números com casas decimais ou trocar a ordem das entradas.