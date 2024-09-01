# Escreva um programa em Python que solicita ao usuário que digite seu nome, o valor do seu salário mensal e o valor do bônus que recebeu, O programa deve, então , imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido. + Com o tratamento de errors. + Loop de tentativas.

# Constante do KPI 2024
CONSTANTE_BONUS = 1000

# Iniciando variáveis booleanas
nome_valido = False
salario_valido = False
bonus_valido = False

try:
    # 1) Solicita ao usuário que digite seu nome
    while not nome_valido:
        try:
            nome = str(input("Insira seu nome: ").strip().title())
            if not nome.replace("'", "").replace(' ', '').isalpha():
                raise ValueError('O nome contém caractéres inválidos.')
        except ValueError as e:
            print(f'ERRO. {e}')
        else:
            print(f'Nome válido registrado: {nome}')
            nome_valido = True

    # 2) Solicita ao usuário que digite o valor do seu salário
    # Converte a entrada para um número de ponto flutuante
    while not salario_valido:
        try:
            salario = float(input("Insira o valor de seu salário mensal: R$").strip().replace(',', '.'))
            if salario < 0:
                raise ValueError('O salário deve ser um número positivo')
        except ValueError as e:
            print(f'Valor inválido. {e}')
        except Exception as e:
            print(f'Erro, {e}')
        else:
            print(f'Salário registrado: R${salario:.2f}')
            salario_valido = True

    # 3) Solicita ao usuário que digite o valor do bônus recebido
    # Converte a entrada para um número de ponto flutuante
    while not bonus_valido:
        try:
            bonus = float(input("Insira o bônus (%): ")) / 100
            if bonus < 0:
                raise ValueError('O bônus deve ser um número positivo')
        except ValueError as e:
            print(f'Valor inválido. {e}')
        except Exception as e:
            print(f'Erro, {e}')
        else:
            print(f'Bônus de {bonus*100}% = {bonus}')
            bonus_valido = True
except KeyboardInterrupt:
    print('\nSistema terminado pelo usuário.')
else:

    # 4) Calcule o valor do bônus final
    bonus_final = bonus * salario

    # 5) Imprima cálculo do KPI para o usuário
    kpi = CONSTANTE_BONUS + bonus_final
    print(f'Cálculo do KPI:\nKPI = 1000 + ({salario} X {bonus}) = R${kpi}')

    # 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
    novo_salario = salario + kpi
    print(f'Saudações {nome}, seu salário agora é de R${novo_salario:.2f}')
finally:
    print('Fim do programa')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Problemas em erros de digitação, como usar vírgula ao invés de ponto para os números com casas decimais ou trocar a ordem das entradas.