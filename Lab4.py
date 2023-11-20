for count in range(0,11,1):
    print(count, end = " ")
print()

for count in range(1,11,1):
    print(count, end = " ")
print()

for count in range(1,11,2):
    print(count, end = " ")
print()

import math
area_of_circle= 0.00
radius=float(input('Enter Radius = '))
if(radius>=0):
    print('valid input')
    area_of_circle= math.pi * radius * radius
    print(area_of_circle)
else:
    print('Invalid Input')
    print()

Length= float(input('Enter Length = '))
Breadth=float(input('Enter Breadth = '))
area_of_rectangle= Length*Breadth
print(area_of_rectangle)

Length=float(input('Enter Length = '))
Breadth=float(input('Enter Breadth = '))
if(Length>0):
    print('valid input')
if(Breadth>0):
    print('valid input')
    area_of_rectangle= Length * Breadth
    print(area_of_rectangle)
else:
    print('Invalid Input')
    print()
