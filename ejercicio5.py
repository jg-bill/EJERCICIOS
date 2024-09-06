#5.-Se requiere un algoritmo para elaborar la planilla de un empleado
#Para ello se dispone de sus horas laboradas en el mes,
#asi como la tarifa por hora.
empleado=input("Ingrese su nombre: ")
ht=int(input("Ingrese horas trabajadas en el mes: "))
ch=float(input("Ingrese costo por horas: "))
#procesamos datos
pt=ht*ch
#imprimir resultados
print ("PAGO")
print ("-"*30)
print ("Sr.",empleado ,"su pago mensual total es: S/.",pt)