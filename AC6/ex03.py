"""
Programação Estruturada
2024.1
25/03/2024
AC6
Prof: Victor Machado
Aluno: Fabrício de Brito
"""


peca1 = input('')
peca2 = input('')

peca1 = peca1.split(' ')
codigo_peca1 = int(peca1[0])
num_peca1 = int(peca1[1])
valor_peca1 = float(peca1[2])
total_peca1 = valor_peca1 * num_peca1

peca2 = peca2.split(' ')
codigo_peca2 = int(peca2[0])
num_peca2 = int(peca2[1])
valor_peca2 = float(peca2[2])
total_peca2 = valor_peca2 * num_peca2


print(f'VALOR A PAGAR: R$ {total_peca1 + total_peca2:.2f}')
