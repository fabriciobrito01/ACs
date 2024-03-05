"""
Programação Estruturada
2024.1
05/03/2024
AC4
Prof: Victor Machado
Aluno: Fabrício de Brito
"""

def ler_nome_usuario():
    """
    Pede para o usuário informar o nome, e retorna uma string.
    """
    return input("Informe o seu nome: ")

def ler_notas():
    """
    Lê e retorna quatro notas do tipo float.
    """
    ap1 = float(input('Informe a nota da AP1: '))
    ap2 = float(input('Informe a nota da AP2: '))
    asub = float(input('Informe a nota da AS: '))
    ac = float(input('Informe a nota da AC: '))
    return ap1, ap2, asub, ac

def validar_notas(ap1, ap2, asub, ac):
    """
    Retorna False se pelo menos uma das notas for menor que zero ou
    maior que dez.
    """
    if ap1 < 0 and ap1 > 10:
        return False

    if ap2 < 0 and ap2 > 10:
        return False

    if asub < 0 and asub > 10:
        return False

    if ac < 0 and ac > 10:
        return False
    return True

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as informadas.
    """
    if asub > ap1:
        return asub, ap2

    if asub > ap2:
        return asub, ap1

    return ap1, ap2

def calcular_media(n1, n2, ac):
    """
    Calcula e retorna a média do usuário.
    """
    return (n1 + n2) * 0.4 + ac * 0.2

def informar_aprovacao(media):
    """
    Informa se o aluno passou ou não na disciplina.
    """
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Você foi reprovado...")

def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()