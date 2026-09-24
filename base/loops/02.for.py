villanos  = ["lex lutor","bane","thanos","joker"]

for villano in villanos:
    print(villanos)
    print(f"{villano} son muy malos")
numeros = [1,2,3,4,5,6]
for numero in numeros:
    # multiplicado = numero * 2 es una manera mas larga
    print(numero * 2 )

for number in range(3):
    print("thank you")



# ejercicio
#Tengo una lista de nuemeros y quwiero encontrar los duplicados de esa lista
# lista,for,dicciomario
# el resultado de 2 : 3 3:2 5:2
lst = [1,2,3,2,4,5,3,2,6,5]
feq = {}

for num in lst:
    if num in feq:
        feq[num] = feq[num] + 1 
    else:
        feq[num] = 1
print(feq)

for key in feq:
    if feq[key] > 1:
        print(key,":", feq[key])