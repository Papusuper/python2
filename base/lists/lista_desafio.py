# if i 
list_pares = []

for i in range(20):
    if i % 2 == 0:
        list_pares.append(i)

print(list_pares)

#compresion de lista 
list_impares = [i for i in range(20) if i % 2 !=0]
print(list_impares)

#segundo ejeccicio 
# listas de rutas
frutas = ["melocoton","uvas","piña","pera","papaya","sandia"]
frutas_sin_duplicados = []

for fruta in frutas:
    if fruta not in frutas_sin_duplicados:
        frutas_sin_duplicados.append(fruta)
print(frutas_sin_duplicados)

#lista de frutas de una manera mas elegante 
frutas_sin_duplicados = set(frutas)
print(frutas_sin_duplicados)
