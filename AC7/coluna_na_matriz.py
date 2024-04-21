'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

C = int(input())
T = input()

soma = 0

matriz = []
for i in range(12):
    vetor = []

    for j in range(12):
        valor = float(input())
        vetor.append(valor)
        matriz.append(vetor)

        if (j == C):
            soma += valor

    vetor = []


if T == 'M':
    media = soma / 12
    print(f'{media:.1f}')
elif T == 'S':
    print(f'{soma:.1f}')
