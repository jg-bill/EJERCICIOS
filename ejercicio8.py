#8.-Elaborar un algoritmo que solicite el número de
#respuestas correctas, incorrectas y en blanco,
#correspondientes a postulantes, y muestre su puntaje
#final considerando, que por cada respuesta correcta
#tendrá 4 puntos, respuestras incorrectas tendrá -1
#y respuestas en blanco tendrá 0.
print("De las 5 preguntas que realizo.")
co=int(input("Ingrese el número de respuestas correctas: "))
inc=int(input("Ingrese el número de respuestas incorrectas: "))
va=int(input("Ingrese el número de respuestas en blanco: "))
bien=co*4
mal=inc*(-1)
nada=va*0
f=bien+mal+nada
print("PUNTAJE FINAL")
print("-"*30)
print("Puntaje: ",f)