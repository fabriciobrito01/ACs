'''
Programação Estruturada
2024.1
12/05/2024
AC9
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

lista = input()
lista = lista.split(" ")

C = int(lista[0])
P = int(lista[1])
F = int(lista[2])

if C * F <= P:
    print("S")

else:
    print("N")
