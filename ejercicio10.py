#10.-Elabore un algoritmo que lea 3 lados de un
#triángulo cualquiera y calcule su área. Considerar:
#si a, b, c son los lados y s el semi perímetro
#A=raíz(s*(s-a)*(s-b)*(s-c))
from math import sqrt
a = float(input("Ingrese la longitud del primer lado del triángulo: "))
b = float(input("Ingrese la longitud del segundo lado del triángulo: "))
c = float(input("Ingrese la longitud del tercer lado del triángulo: "))
s = (a + b + c) / 2
print("EL SEMI PERIMETRO ES: ",s)
area = sqrt(s * (s - a) * (s - b) * (s - c))
print("-"*30)
print("El área del triángulo es: ",area)