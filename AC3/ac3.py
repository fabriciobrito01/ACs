'''
Programação Estruturada
2024.1
18/03/2024
AC3
Prof: Victor Machado
Aluno: Fabrício de Brito
'''


def determina_tipo_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return 'Equilátero'

        elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
            return 'Isósceles'

        elif lado1 != lado2 != lado3:
            return 'Escaleno'
    else:
        return 'Não é um triângulo'


def teste_dia_semana(num):
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


def main():
    print(determina_tipo_triangulo(4, 4, 4))
    print(determina_tipo_triangulo(2, 4, 4))
    print(determina_tipo_triangulo(3, 4, 5))
    print(determina_tipo_triangulo(1, 1, 4))
    print(teste_dia_semana(2))
    print(teste_dia_semana(6))
    print(teste_dia_semana(7))
    print(teste_dia_semana(10))


main()
