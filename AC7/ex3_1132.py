'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito

Múltiplos de 13 - 1132
'''

x = int(input())
y = int(input())

if x > y:
    maior = x
    menor = y

else:
    menor = x
    maior = y

soma_nao_divisiveis = 0
for c in range(menor, maior+1):
    if c % 13 != 0:
        soma_nao_divisiveis += c

print(soma_nao_divisiveis)
