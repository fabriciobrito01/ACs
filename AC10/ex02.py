'''
Programação Estruturada
2024.1
19/05/2024
AC10
Prof: Victor Machado
Aluno: Fabrício de Brito
'''

import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    index = 0
    cases = int(data[index])
    index += 1
    
    for case in range(cases):
        if case > 0:
            print()
        
        avres = defaultdict(int)
        total = 0
        
        while index < len(data) and data[index].strip() == '':
            index += 1
        
        while index < len(data) and data[index].strip() != '':
            avre = data[index].strip()
            avres[avre] += 1
            total += 1
            index += 1
        
        for tree in sorted(avres):
            percentage = (avres[tree] / total) * 100
            print(f"{tree} {percentage:.4f}")

if __name__ == "__main__":
    main()

