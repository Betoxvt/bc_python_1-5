# Escreva um programa em Python que solicita ao usuário que digite seu nome, o valor do seu salário mensal e o valor do bônus que recebeu, O programa deve, então , imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido. + Com o tratamento de errors. + Loop de tentativas. + type hint, função, dicionários.


def linha() -> str:
    print('-'*50)


def titulo(mensagem=' ') -> str:
    linha()
    print(mensagem.center(50))
    linha()


def inserir_nome_valido() -> str:
    while True:
        try:
            nome: str = str(input("\nInsira seu nome: ").strip().title())
            if not nome.replace("'", "").replace(' ', '').isalpha():
                raise ValueError('O nome contém caractéres inválidos.')
        except ValueError as e:
            print(f'\n\033[31mERRO. {e}.\033[m')
        else:
            print(f'\n\033[32mNome válido\033[m')
            return nome
        

def inserir_numero_float_valido(mensagem='ponto flutuante') -> float:
    while True:
        try:
            numero: float = float(input(f'\nInsira o valor para {mensagem}: ').strip().replace(',', '.'))
            if numero < 0:
                raise ValueError
        except ValueError:
            print(f'\n\033[31mERRO. O valor deve ser um número positivo.\033[m')
        else:
            print(f'\n\033[32mValor de {mensagem} válido\033[m')
            return numero
        

def calcular_kpi(salario='0', bonus='0') -> float:
    CONSTANTE_BONUS: int = 1000
    kpi: float = CONSTANTE_BONUS + (bonus * salario)
    return kpi


# Programa principal
try:
    titulo('Calculadora KPI 2024')
    # 1) Solicita ao usuário que digite seu nome
    nome: str = inserir_nome_valido()
    # 2) Solicita ao usuário que digite o valor do seu salário
    # Converte a entrada para um número de ponto flutuante
    salario: float = inserir_numero_float_valido('salário')
    # 3) Solicita ao usuário que digite o valor do bônus recebido
    # Converte a entrada para um número de ponto flutuante
    bonus: float = inserir_numero_float_valido('bônus')   
except KeyboardInterrupt:
    print('\n\033[31mSistema terminado pelo usuário.\033[m')
else:
    # 4) Calcule o valor do bônus final
    kpi: float = calcular_kpi(salario, bonus)
    # 5) Imprima cálculo do KPI para o usuário
    print(f'\nKPI = 1000 + ({salario} X {bonus}) = {kpi}')
    # 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
    print(f'\n\033[34mSaudações {nome}, seu salário é R$ {salario:.2f} e seu bônus R$ {kpi:.2f}\033[m\n')
finally:
    titulo('Fim do programa')
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Problemas em erros de digitação, como usar vírgula ao invés de ponto para os números com casas decimais ou trocar a ordem das entradas.
