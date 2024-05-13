'''
Programação Estruturada
2024.1
12/05/2024
AC9
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

soma = 0

for n in range(int(input())):
    horas, kmh = map(int,input().split())
    soma += (kmh, horas)

print(soma)