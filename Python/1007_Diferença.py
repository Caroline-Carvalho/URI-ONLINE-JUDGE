'''
URI Online Judge | 1008 - Salário
@author Caroline Carvalho
'''
import sys

number = int(sys.stdin.readline())
horasTrabalhadas = int(sys.stdin.readline())
valorHora = float(sys.stdin.readline())

salary = horasTrabalhadas * valorHora

print('NUMBER = %d' % number)
print('SALARY = U$ %.2f' % salary)