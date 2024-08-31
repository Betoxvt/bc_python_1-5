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
            while not nome_valido:
                nome = str(input("Insira seu nome: ").strip().title())
                if nome.replace("'", "").replace(' ', '').isalpha():
                    nome_valido = True
                else:
                    print('O nome contém caractéres inválidos.')
        except Exception as e:
            print(f'Erro, {e}')
            nome_valido = False
        else:
            print(f'Nome válido registrado: {nome}')
            nome_valido = True

    # 2) Solicita ao usuário que digite o valor do seu salário
    # Converte a entrada para um número de ponto flutuante
    while not salario_valido:
        try:
            while not salario_valido:
                salario = float(input("Insira o valor de seu salário mensal: R$").strip().replace(',', '.'))
                if salario < 0:
                    print('O salário deve ser um número positivo')
                else:
                    salario_valido = True
        except ValueError:
            print('Entrada inválida. O salário deve ser um número')
            salario_valido = False
        except Exception as e:
            print(f'Erro, {e}')
            salario_valido = False
        else:
            print(f'Salário registrado: R${salario:.2f}')
            salario_valido = True

    # 3) Solicita ao usuário que digite o valor do bônus recebido
    # Converte a entrada para um número de ponto flutuante
    while not bonus_valido:
        try:
            while not bonus_valido:
                bonus = float(input("Insira o bônus (%): ")) / 100
                if bonus < 0:
                    print('O bônus deve ser um número positivo')
                else:
                    bonus_valido = True
        except ValueError:
            print('O bônus deve ser um número')
            bonus_valido = False
        except Exception as e:
            print(f'Erro, {e}')
            bonus_valido = False
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