'''
URI Online Judge | 1009 - Salário com Bônus
@author Caroline Carvalho
'''
import sys

nome = sys.stdin.readline()
salario = float(sys.stdin.readline())
montanteVendas = float(sys.stdin.readline())

total = salario + (0.15 * montanteVendas)

print('TOTAL = R$ %.2f' % total)