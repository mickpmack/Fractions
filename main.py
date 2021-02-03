from factors import *
from fractions import *
from test import *
import time, sys, random


# k=find_hcf(-12,72)
# print(k)
# sys.exit(0)


p=fraction(2,4)
q=fraction(1,3)
r=p+q
print(f'{p} + {q} = {r}')
r=p*q
print(f'{p} * {q} = {r}')
r=p/q
print(f'{p} / {q} = {r}')
r=p-q
print(f'{p} + {q} = {r}')

unittest_factors()

unittest_fractions()

sys.exit(0)

