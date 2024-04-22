'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito

Aumento de salário - 1048
'''

salario = float(input(''))

if salario <= 400 > 0:
    aumento = 0.15 

elif salario <= 800 > 400:
    aumento = 0.12

elif salario <= 1200 > 800:
    aumento = 0.10

elif salario <= 2000 > 1200:
    aumento = 0.07

elif salario > 2000:
    aumento = 0.04

reajuste = salario * aumento
novo_salario = salario + salario * aumento

print(f'''Novo salario: {novo_salario:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: {int(aumento * 100)} %''')
