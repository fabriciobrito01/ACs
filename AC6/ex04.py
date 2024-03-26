"""
Programação Estruturada
2024.1
25/03/2024
AC6
Prof: Victor Machado
Aluno: Fabrício de Brito
"""

numeros = input('').split(' ')

a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])


maior_ab = (a + b + abs(a - b)) / 2
maior_ac = (a + c + abs(a - c)) / 2
maior_bc = (b + c + abs(b - c)) / 2


if maior_ab == maior_ac:
    print(a, 'eh o maior')

elif maior_ab == maior_bc:
    print(b, 'eh o maior')

else:
    print(c, 'eh o maior')
