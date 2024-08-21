# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    n1 = int(input("Inserir um número inteiro: "))
    n2 = int(input("Inserir outro número inteiro: "))
    resultado = n1 // n2
    print(f'A divisão inteira de {n1} por {n2} é {resultado}')
except ZeroDivisionError:
    print('Erro de divisão por zero')
except KeyboardInterrupt:
    print('OK, pulamos este exercício')
except ValueError as e:
    print(e)
else:
    print('Tudo ocorreu bem')
finally:
    print('O importante é participar!')
print('-='*30)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

try:
    data_do_user = input("Insira uma data no formato dd/mm/aaaa: ")
    data_lista = data_do_user.split('/')
    print(f'Dia {int(data_lista[0])}')
    print(f'Mês {int(data_lista[1])}')
    print(f'Ano {(data_lista[2])}')
except IndexError:
    print('Ops, por favor verifique o formato dd/mm/aaaa')
except ValueError:
    print('Utilize apenas números e no formato dd/mm/aaaa')
except:
    print('Ops! Algo deu errado.')
print('-='*30)


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação