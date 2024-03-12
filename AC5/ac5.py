'''
Programação Estruturada
2024.1
12/03/2024
AC5
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

import random


def main():

    aventureiro_vida = 100
    aventureiro_atk = random.randint(10, 20)
    aventureiro_def = random.randint(1, 5)

    monstro_vida = random.randint(60, 80)
    monstro_atk = random.randint(20, 30)

    print(f'Aventureiro: vida {aventureiro_vida} - atk {aventureiro_atk} - def {aventureiro_def}' )
    print(f'Monstro: vida {monstro_vida} - atk {monstro_atk}')

    rodada = 1
    while aventureiro_vida > 0 and monstro_vida > 0:
        print('Rodada', rodada)
        monstro_vida = monstro_vida - random.randint(1, aventureiro_atk)
        dano_monstro = random.randint(1, monstro_atk) - aventureiro_def

        if dano_monstro > 0:
            aventureiro_vida = aventureiro_vida - dano_monstro

        if monstro_vida <= 0:
            print('O montro morreu!')
            break
        if aventureiro_vida <= 0:
            print('Você morreu!')
            break

        print(f'Aventureiro: vida {aventureiro_vida} - atk {aventureiro_atk} - def {aventureiro_def}' )
        print(f'Monstro: vida {monstro_vida} - atk {monstro_atk}')
        rodada += 1


main()
