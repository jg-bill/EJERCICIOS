name= input ( " Ingrese nombre del universitario: ")
ResCorr= int (input ( " INGRESE NUMERO DE PARTIDOS GANADOS: "))
ResIncorr= int (input ( " INGRESE NUMERO DE PARTIDOS EMPATADOS: "))
ResBlanc= int (input ( " INGRESE NUMERO DE PARTIDOS PERDIDOS: "))
puntajFinal = (ResCorr*3)+ (ResIncorr*-1)+(ResBlanc*0)

print ( " EL PUNTAJE FINAL DEL UNIVERSITARIO ", name, " Y EL PUNTAJE FINAL ES ", puntajFinal)