'''
URI Online Judge | 1002 - Área do Círculo
@author Caroline Carvalho
'''

import sys

raio = float(sys.stdin.readline())
area = round(3.14159 * raio**2, 4)

print('A=%.4f' %area)
