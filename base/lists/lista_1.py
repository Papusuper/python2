frutas = ["melocoton","uvas","piña","pera","papaya","sandia"]
print(frutas)
# copia de valores de una lista a otra lista 
frutas2 = frutas.copy() 
frutas2[0] = "manzana"
print(frutas2)
print(frutas) 
# tamaño de la lista
print(len(frutas))
#acceder a un elemento de una lista 
print(frutas[5])
#accer al ultimo elemento
print(frutas[-2])
#sacar el rango
print(frutas[1:4])
#sacar desde posicion 2 hasta la ultima, o desde cualquiera 
print(frutas[2:])
#sacar desde el final hasta la posicion 3 
print(frutas[:-3]) 
#sacar solo hasta determinado vbalor 
print(frutas[:4]) 
#manera de remplazar un dato de una lista 
frutas[1:2] = ["mora","guanabana"]
print(frutas)