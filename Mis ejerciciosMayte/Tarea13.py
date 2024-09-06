from math import *
a=int(input( " INGRESA EL VALOR a: "))
b=int(input( " INGRESA EL VALOR b: "))
c=int(input( " INGRESA EL VALOR c: "))

mayte=sqrt((b**2) - (4*(a*c)))
x1=(-b+mayte)/(2*a)
x2=(-b-mayte)/(2*a)



print (" x1 es igual a: ",  x1, " x2 es igual a ", x2 )

if ((a*(x2**2))+(b*x2)+c == 0):
    print("x1 es correcto");
else: 
    print((a*(x1**2))+(b*x1)+c)
