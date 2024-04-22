'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito

Ordenação por Tamanho - 1244
'''

n = int(input())

for c in range(n):
    s = input()
    s_lista = s.split(" ")
    s_ordem = sorted(s_lista, key=len, reverse=True)
    print(" ".join(s_ordem))
