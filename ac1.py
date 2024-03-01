'''
Programação Estruturada 2024.1
04/03/2024
AC1 - ex1 e ex2
Professor: Victor Machado
Aluno: Fabrício de Brito
'''

 # Ex1
def equacao():
    a = int(input('Informe o parâmetro a da equação: '))
    b = int(input('Informe o parâmetro b da equação: '))
    c = int(input('Informe o parâmetro c da equação: '))
    r1 = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    r2 = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    print(f'A primeira raiz é {r1}')
    print(f'A segunda raiz é {r2}')

# Ex2
def ano_bissexto():
    print('Descubra se um ano é bissexto...')
    ano = int(input('Digite um ano: '))
    print (ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0)

def main():
    equacao()
    ano_bissexto()
    

main()