# Escreva um programa em Python que solicita ao usuário que digite seu nome, o valor do seu salário mensal e o valor do bônus que recebeu, O programa deve, então , imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

# Constante do KPI 2024
CONSTANTE_BONUS = 1000

# Solicita o nome do usuário
nome = str(input("Insira seu nome: ").strip().title())

# Solicita o salário do usuário e transforma em ponto flutuante
salario = float(input("Insira o valor de seu salário mensal: R$"))

# Solicita o bônus em porcentagem e transforma em ponto flutuante
bonus_percent = float(input("Insira o bônus (%): ")) / 100

# Armazena os cálculos em variáveis
bonus = bonus_percent * salario
kpi = CONSTANTE_BONUS + bonus
novo_salario = salario + kpi

# Imprime um texto com o solicitado pelo desafio
print(f'Saudações {nome}, seu salário agora é de R${novo_salario:.2f}')