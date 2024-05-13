'''
Programação Estruturada
2024.1
12/05/2024
AC9
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

N = int(input())
for i in range (N):
    v = 0
    produtos = {}
    
    M = int(input())
    for c in range (M):
        lista = input().split()
        produtos[lista[0]] = float(lista[1])
    
    P = int(input())
    if 1 <= P <= M:
        for x in range (P):
            item, qtd = input().split() 
            v += produtos[item] * int(qtd)
    
    print(f'R$ {v:.2f}')