"""
Programação Estruturada
2024.1
25/03/2024
AC6
Prof: Victor Machado
Aluno: Fabrício de Brito
"""

p1 = input('').split(' ')
p2 = input('').split(' ')

x1 = float(p1[0])
y1 = float(p1[1])

x2 = float(p2[0])
y2 = float(p2[1])

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'{distancia:.4f}')
