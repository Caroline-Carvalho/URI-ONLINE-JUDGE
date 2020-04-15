'''
URI Online Judge | 1010 - Cálculo Simples
@author Caroline Carvalho
'''
import sys

p1, numP1, valP1 = sys.stdin.readline().split(" ")
p1 = int(p1)
numP1 = int(numP1)
valP1 = float(valP1)

p2, numP2, valP2 = sys.stdin.readline().split(" ")
p2 = int(p2)
numP2 = int(numP2)
valP2 = float(valP2)

total = (numP1 * valP1) + (numP2 * valP2)

print('VALOR A PAGAR: R$ %.2f' % total)