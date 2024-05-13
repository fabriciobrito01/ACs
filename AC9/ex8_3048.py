'''
Programação Estruturada
2024.1
12/05/2024
AC9
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

lista = []

for c in range(int(input())):
    num = input()
    
    if not lista:
        lista.append(num)
    
    elif num != lista[-1]:
        lista.append(num)

print(len(lista))
