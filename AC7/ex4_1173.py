'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito

Preenchimento de Vetor I - 1173
'''

v = int(input())

if v <= 50: 
    i = 0
    while i < 10:
        x = v
        v = v * 2
        print(f'N[{i}] = {x}')
        i += 1
