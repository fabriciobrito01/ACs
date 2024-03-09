'''
Programação Estruturada
2024.1
11/03/2024
AC2
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

# Ex1


def eq_seg_grau(a, b, c):
    '''Recebe 3 valores e retorna as raízes de uma equação de segundo grau.'''
    r1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    r2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print('A primeira raiz é ', r1)
    print('A segunda raiz é ', r2)


def bissexto(ano):
    '''Recebe um ano e retorna um valor booleano, informando se é bissexto ou não.'''
    bis = ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0
    return bis


# Ex2


def calcula_salario(valor_hora, num_horas, irpf=0.275):
    '''Recebe dois parâmetros posicionais reais e um parâmetro-chave e
       calcula um salário líquido através deles.'''
    salario = (valor_hora * num_horas) - ((valor_hora * num_horas) * irpf)
    return salario


def main():
    '''Chama as funções utilizadas.'''
    eq_seg_grau(1, -6, 8)
    print('O ano é bissexto? ', bissexto(1900))
    print('O salário líquido é de R$', calcula_salario(100, 100))


main()
