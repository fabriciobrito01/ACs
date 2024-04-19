'''
Programação Estruturada
2024.1
21/04/2024
AC7
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

x = int(input(''))
y = int(input(''))

s = x + y

soma_nao_divisiveis = 0
for c in range (s):
    if not c % 13 == 0:
        soma_nao_divisiveis += 1
print(soma_nao_divisiveis)