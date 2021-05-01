#!/usr/bin/env python3 

f = lambda x  : x**2 

numbers = range(15)
squared_numbers = [num * num for num in numbers]

with open('data.dat','w') as out:
  for x in range(15):
    line = f'{x} {f(x)}'
    out.write(f'{line}\n')

# with open('data.dat','w') as out:
#   for num,sq in zip(numbers ,squared_numbers):
#     line = f'{num} {sq}'
#     out.write(f'{line}\n')