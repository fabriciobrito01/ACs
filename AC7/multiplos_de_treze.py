'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

x = int(input())
y = int(input())


soma_nao_divisiveis = 0
for c in range(x, y+1):
    if c % 13 != 0:
        soma_nao_divisiveis += c

print(soma_nao_divisiveis)
