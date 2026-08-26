#opeaaciones de listas
frutas = ["melocoton","uvas","piña","pera","papaya","sandia"]
#Agregar un elemento al final de la lista 
frutas.append("kiwi")
print(frutas)
#insectar a la lista en una pocosoion especifica 
frutas.insert(1,"melon")
print(frutas)
#revomer un elemento de la lista 
frutas.revome("piña")
#remover un elemento de la lista de una posicion
frutas.pop(3) 
#remover el ultimo elemento 
frutas.pop()
#remover todo de una lista 
frutas.clear()
print(frutas)

#recorrer una lista 
frutas = ["melocoton","uvas","piña","pera","papaya","sandia"]
for fruta in frutas:
         print(fruta)    
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
        print(numero * 2)
        print(numero ** 2)
        print(numero ** 3)

# recorrer una lista con un rango de indices 
for i in range(len(frutas)):
        print(frutas[i])

#comprension de lista 
#new_list = []
#for fruta in frutas:
    ##new_list.append(fruta)
    #esta era la manera larga de hacerlo


#manera rapida y corta 
new_list = [x for x in frutas if "a" in x]
print(new_list)

new_list_numeros = [x for x in numeros if x % 2 == 0]
print(new_list_numeros)

        