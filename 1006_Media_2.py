'''
URI Online Judge | 1006 - Média 2
@author Caroline Carvalho
'''

import sys

a = float(sys.stdin.readline())
b = float(sys.stdin.readline())
c = float(sys.stdin.readline())

media = ((2 * a) + (3 * b) + (5 * c)) / 10

print('MEDIA = %.1f' %media)
