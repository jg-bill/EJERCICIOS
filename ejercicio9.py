#9.-Elabora un algoritmo que permita ingresar el número
#de partios ganados, perdidos y empatados, por
#Universitario de deportes en el torneo de apertura, se
#debe de mostrar su puntaje, teniendo en cuenta que por
#cada partido ganado obtendrá 3 puntos, empatado 1 punto
#y perdido 0 puntos.
print("De las 5 preguntas que realizo.")
vi=int(input("Ingrese el número de partidos ganados: "))
em=int(input("Ingrese el número de partidos empatados: "))
pe=int(input("Ingrese el número de partidos perdidos: "))
victoria=vi*3
empate=em*1
perdido=pe*0
f=victoria+empate+perdido
print("PUNTAJE FINAL")
print("-"*30)
print("Puntaje: ",f)