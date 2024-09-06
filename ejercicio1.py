#1.-Ingrese el numero de horas trabajadas y el costo por horas, calcular el pago total.
#declaramos variables
nombre=input("Ingrese su nombre: ")
ht=int(input("Ingrese horas trabajadas: "))
ch=float(input("Ingrese costo por horas: "))
#procesamos datos
pt=ht*ch
#imprimir resultados
print ("Horas calculadas del trabajador")
print ("-"*30)
print ("Sr.",nombre ,"su pago total es: S/.",pt)