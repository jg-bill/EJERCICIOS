nombre = input ( " INGRESAR NOMBRE DEL ALUMNO: ")
num1= float (input( "INGRESAR PRIMERA NOTA: "))
num2= float (input( "INGRESAR SEGUNDA NOTA: "))
num3= float (input( "INGRESAR TERCERA NOTA: "))

prom = (num1 + num2 + num3)/3
print ( " EL PROMEDIO DEL ALUMNO", nombre, " ES ", round(prom,0))