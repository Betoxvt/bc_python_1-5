# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# try:
#     n1 = int(input('Insira o primeiro número: '))
#     n2 = int(input('Insira o segundo número: '))
#     resposta = n1 + n2
#     print(f'A Soma é {resposta}')
# except:
#     pass
# print('-='*30)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# try:
#     n1 = int(input('Insira um número: '))
#     resposta = n1 % 5
#     print(f'O resto de {n1}/5 é {resposta}')
# except:
#     pass
# print('-='*30)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# try:
#     n1 = int(input('Insira um número: '))
#     n2 = int(input('Insira outro número: '))
#     resposta = n1 * n2
#     print(f'A multiplicação entre {n1} e {n2} é {resposta}')
# except:
#     pass
# print('-='*30)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# try:
#     n1 = int(input("Inserir um número inteiro: "))
#     n2 = int(input("Inserir outro número inteiro: "))
#     resultado = n1 // n2
#     print(f'A divisão inteira de {n1} por {n2} é {resultado}')
# except ZeroDivisionError:
#     print('Erro de divisão por zero')
# except KeyboardInterrupt:
#     print('OK, pulamos este exercício')
# except ValueError as e:
#     print(e)
# else:
#     print('Tudo ocorreu bem')
# finally:
#     print('O importante é participar!')
# print('-='*30)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# try:
#     n1 = int(input('Insira um número: '))
#     resposta = n1 ** 2
# except:
#     pass
# else:
#     print(f'{n1} ao quadrado é {resposta}')
# print('-='*30)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# try:
#     n1 = float(input('1º número: ').strip().replace(',', '.'))
#     n2 = float(input('2º número: ').strip().replace(',', '.'))
#     ad = n1 + n2
# except Exception as e:
#     print(f'\033[31mOcorrou um erro, {e}\033[m')
#     pass
# else:
#     print(f'A adição entre {n1} e {n2} é igual a {ad}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# try:
#     n1 = float(input('1º número: ').strip().replace(',', '.'))
#     n2 = float(input('2º número: ').strip().replace(',', '.'))
#     µ = (n1+n2)/2
# except Exception as e:
#     print(f'\033[31mOcorrou um erro, {e}\033[m')
#     pass
# else:
#     print(f'A média artimética simples dos números inseridos é {µ}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# try:
#     base = float(input('Base: ').strip().replace(',', '.'))
#     expoente = float(input('Expoente: ').strip().replace(',', '.'))
#     pot = base**expoente
# except Exception as e:
#     print(f'\033[31mOcorrou um erro, {e}\033[m')
#     pass
# else:
#     print(f'O resultado da potenciação de base {base} pelo expoente {expoente} é {pot}')


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# CONS1 = 1.8
# CONS2 = 32

# try:
#     tc = float(input('Insira a temperatura em Celsius: '))
#     tf = tc*CONS1 + CONS2
# except Exception as e:
#     print(f'\033[31mERROR. {e}\033[m')
# else:
#     print(f'Convertendo {tc}ºC fica {tf}ºF')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# from math import pi

# try:
#     r = float(input('Raio (cm): ').strip().replace(',', '.'))
#     a = pi*r**2
# except Exception as e:
#     print(f'\033[31mERROR. {e}\033[m')
# else:
#     print(f'A área do círculo com  raio {r}cm é {a}cm²')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# txt = input('Digite: ').upper()
# print(txt)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# txt = input('Seu nome completo: ').lower()
# print(txt)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# txt = input('Digite uma frase: ').strip()
# print(f'Sem espaços no início e fim: {txt}')
# print(f'Sem espaço nenhum: {txt.replace(' ', '')}')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# try:
#     data_do_user = input("Insira uma data no formato dd/mm/aaaa: ")
#     data_lista = data_do_user.split('/')
#     print(f'Dia {int(data_lista[0])}')
#     print(f'Mês {int(data_lista[1])}')
#     print(f'Ano {(data_lista[2])}')
# except IndexError:
#     print('Ops, por favor verifique o formato dd/mm/aaaa')
# except ValueError:
#     print('Utilize apenas números e no formato dd/mm/aaaa')
# except:
#     print('Ops! Algo deu errado.')
# print('-='*30)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# txt1 = input('Primeira string: ')
# txt2 = input('Segunda string: ')
# concat = txt1+txt2
# print(concat)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# try:
#     b1 = bool(input('Primeira: '))
#     b2 = bool(input('Segunda: '))
# except Exception as e:
#     print(f'\033[31mERROR. {e}\033[m')
# else:
#     print(b1 and b2)
    
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# try:
#     b1 = bool(input('Primeira: '))
#     b2 = bool(input('Segunda: '))
# except Exception as e:
#     print(f'\033[31mERROR. {e}\033[m')
# else:
#     print(b1 or b2)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# try:
#     while True:
#         value = input('V ou F: ').strip().upper()[0]
#         if value == 'V':
#             v = True
#             inv = 'F'
#             break
#         elif value == 'F':
#             v = False
#             inv = 'V'
#             break
#         else:
#             print('Não entendi... V ou F?')
# except Exception as e:
#     print(f'\033[31mERROR. {e}\033[m')
# else:
#     iv = not v
#     print(f'Você digitou {value} que é {v}, e inverso é {inv}, ou seja, {iv}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# n1 = int(input('n1: '))
# n2 = int(input('n2: '))
# print(f'São iguais? {n1 == n2}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# n1 = int(input('n1: '))
# n2 = int(input('n2: '))
# print(f'São diferentes? {n1 != n2}')

# #### try-except e if

# 21: Conversor de Temperatura

# C1 = 32
# C2 = 9/5

# print('Qual a unidade de temperatura que você quer converter?')
# print('[1] Celsius')
# print('[2] Fahrenheit')

# try:
#     opt = int(input('Sua opção: '))
# except Exception as e:
#     print(f'\033[31mERROR. {e}\033[m')
# else:
#     if opt == 1:
#         try:
#             tc = float(input('Insira a temperatura em Celsius: '))
#             tf = tc*C2 + C1
#         except Exception as e:
#             print(f'\033[31mERROR. {e}\033[m')
#         else:
#             print(f'Convertendo {tc}ºC fica {tf}ºF')
#     elif opt == 2:
#         try:
#             tf = float(input('Insira a temperatura em Fahrenheit: '))
#             tc = (tf - C1) * C2**-1
#         except Exception as e:
#             print(f'\033[31mERROR. {e}\033[m')
#         else:
#             print(f'Convertendo {tf}ºF fica {tc}ºC')
#     else:
#         print('\033[31mOpção inválida\033[m')

# 22: Verificador de Palíndromo

# txt = input('Insira o texto: ')
# txt1 = txt.upper().replace(' ', '')
# txt2 = txt.upper().replace(' ', '')[::-1]
# print(f'Você digitou {txt}\nAjeitando fica {txt1}\nAo contrário ficou {txt2}\nÉ palindromo? {txt1 == txt2}')

# 23: Calculadora Simples

# while True:
#     print('-='*20)
#     print('Calculadora simplona'.center(40))
#     print('-='*20)
#     try:
#         n1 = float(input('Número: '))
#         o = input('Operação: ')
#         n2 = float(input('Número: '))
#     except Exception as e:
#         print(f'\033[31mERROR. {e}\033[m')
#     else:
#         try:
#             if o == '+':
#                 r = n1+n2
#             elif o == '-':
#                 r = n1-n2
#             elif o in 'x*X.':
#                 r = n1*n2
#             elif o in '/÷':  # and n2 != 0:
#                 r = n1/n2
#             else:
#                 print('Perdão não faço este tipo de operação')
#         except ZeroDivisionError:
#             print('\033[31mNão é possível dividir por ZERO\033[m')
#         else:
#             print(f'{n1} {o} {n2} = {r}')
#         finally:
#             mais = input('Quer continuar? [S/N] ').upper().strip()[0]
#             if mais == 'N':
#                 break

# 24: Classificador de Números 

# PAR ou IMPAR? PRIMO?

# try:
#     n = int(input('Digite um número: '))
# except (TypeError, ValueError):
#     print('Apenas números inteiros)
# except KeyboardInterrupt:
#     print('Terminado pelo usuário')
#     break
# else:
#     if n%2 == 0:
#         print('É par!')
#     else:
#         print('É ímpar!')
#     c = 0
#     for i in range (1, n+1):
#         if n%i == 0:
#             c += 1
#     if c == 2 and n >=2:
#         print ('É primo!')
#     else:
#         print('Não é primo!')
        
# Organizar em ordem crescente no input, 5 números

# cresc = []
# for i in range(5):
#     n = int(input(f'Digite o {i+1}º número: '))
#     if i == 0 or n > cresc[-1]:
#         cresc.append(n)
#         print(f'{n} inserido ao final da lista')
#     else:
#         p = 0
#         while p < len(cresc):
#             if n <= cresc[p]:
#                 cresc.insert(p, n)
#                 print(f'{n} inserido na posição {p} da lista')
#                 break
#             p += 1
# print(cresc)

# 25: Conversão de Tipo com Validação

# try:
#     txt = input('Digite algo: ').strip().replace(',', '.')
# except KeyboardInterrupt:
#     print('\nTerminado pelo usuário')
# else:
#     try:
#         inteiro = int(txt)
#     except (ValueError, TypeError):
#         print('Não é um número inteiro')
#         try:
#             ponto = float(txt)
#         except (ValueError, TypeError):
#             print('Não é um número de ponto flutuante')
#         else:
#             print('É um número de ponto flutuante')
#     else:
#         print('É um número inteiro')
        