#4.-Hallar la potencia de un número y la raíz cuadrado de otro
from math import *
from math import sqrt
base=int(input("Ingrese la base: "))
exponente=int(input("Ingrese el exponente: "))
numero=int(input("Ingrese un número: "))
raiz = sqrt(numero)
resultado=pow(base, exponente)
print("POTENCIA Y RAIZ")
print("-"*25)
print("Base: ",base)
print("Exponente: ",exponente)
print("Resultado: ",resultado)
print("Raiz cuadrada ",raiz)
