#definimos los 3 lados, luego hallamos el semiperimetro = suma de los lados / 2 , luego aplicamos la formula para hallar el area
from math import *
L1= float ( input ( " INGRESAR PRIMER LADO: "))
L2= float ( input ( " INGRESAR SEGUNDO LADO: "))
L3= float ( input ( " INGRESAR TERCER LADO: "))
SP= (L1 + L2+ L3)/2
A= sqrt (SP*(SP-L1)*(SP-L2)*(SP-L3))

print ("EL AREA ES IGUAL A: ", A)
