'''
Programação Estruturada
2024.1
18/03/2024
AC3
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

# Ex1
def determina_tipo_triangulo(lado1, lado2, lado3):
    '''Recebe 3 lados de um triângulo e informa o tipo de triângulo ou se não é um triângulo.'''
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return 'Equilátero'

        elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
            return 'Isósceles'

        elif lado1 != lado2 != lado3:
            return 'Escaleno'
    else:
        return 'Não é um triângulo.'


# Ex2
def teste_dia_semana(num):
    '''Recebe um número inteiro e retorna o dia da semana equivalente, ou uma string vazia caso o número seja inválido.'''
    if num == 1:
        return 'Domingo'
    elif num == 2:
        return 'Segunda-feira'
    elif num == 3:
        return 'Terça-feira'
    elif num == 4:
        return 'Quarta-feira'
    elif num == 5:
        return 'Quinta-feira'
    elif num == 6:
        return 'Sexta-feira'
    elif num == 7:
        return 'Sábado'
    else:
        return ''


# Ex3
def soma(n1, n2):
    '''Recebe dois valores e informa o resultado da soma entre eles.'''
    op_soma = n1 + n2
    return op_soma


def subtração(n1, n2):
    '''Recebe dois valores e informa o resultado da subtração entre eles.'''
    op_subrtacacao = n1 - n2
    return op_subrtacacao


def multiplicacao(n1, n2):
    '''Recebe dois valores e informa o resultado da multiplicação entre eles.'''
    op_multiplicacao = n1 * n2
    return op_multiplicacao


def divisao(n1, n2):
    '''Recebe dois valores e informa o resultado da divisão entre eles.'''
    op_divisao = n1 / n2
    return op_divisao


def cli():
    '''Lê dois números e uma operação e exibe na tela o valor do resultado, 
       ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações.'''
    n1 = float(input('Informe um número: '))
    n2 = float(input('Informe outro número: '))
    operacao = str(input('Informe a operação: '))

    if operacao == 'soma':
        print(soma(n1, n2))

    elif operacao == 'subtração':
        print(subtração(n1, n2))

    elif operacao == 'multiplicação':
        print(multiplicacao(n1, n2))

    elif operacao == 'divisão':
        print(divisao(n1, n2))

    else:
        print('Operação inválida.')


def main():
    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))
    print('=' * 30)
    print(teste_dia_semana(2))
    print(teste_dia_semana(6))
    print(teste_dia_semana(7))
    print(teste_dia_semana(9))
    print('=' * 30)
    cli()


main()
