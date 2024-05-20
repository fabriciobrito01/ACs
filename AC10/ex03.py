'''
Programação Estruturada
2024.1
19/05/2024
AC10
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

import math
import sys

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    index = 0
    while index < len(data):
        N = int(data[index])
        index += 1
        
        H, C, L = map(int, data[index].split())
        index += 1
    
        altura_total = N * H
        
        comprimento_total = N * C
        
        hipotenusa = math.sqrt(altura_total ** 2 + comprimento_total ** 2)
        
        area_cm2 = hipotenusa * L
        
        area_m2 = area_cm2 / 10000
        
        print(f"{area_m2:.4f}")

if __name__ == "__main__":
    main()
