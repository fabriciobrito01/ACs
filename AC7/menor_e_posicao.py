'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

N = int(input())
valores = input()

vetor = valores.split(' ')

menor = int(vetor[0])
pos = 0

if 1 < N < 1000:
    for c in range(N):
        vetor[c] = int(vetor[c])
        if vetor[c] < menor:
            menor = vetor[c]
            pos = c

    print(f'Menor valor: {menor}')
    print(f'Posicao: {pos}')
