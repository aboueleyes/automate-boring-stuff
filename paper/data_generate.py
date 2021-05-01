#!/usr/bin/env python3 

f = lambda x  : x**2 


with open('data.dat','w') as out:
  for x in range(15):
    line = f'{x} {f(x)}'
    out.write(f'{line}\n')
