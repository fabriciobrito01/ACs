'''
Programação Estruturada
2024.1
12/05/2024
AC9
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

T = int(input())

if 1 <= T <= 4:
    A, B, C, D, E = input().split(' ')

    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    E = int(E)

    numeros = [A,B,C,D,E]
    print(numeros.count(T))
