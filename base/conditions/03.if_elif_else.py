# expresion que se evalua y devuelve falso o verdadero 
# IF condicion, si la condicion es verdader, ejecuta las instrucciones que esten debajo del if, sino se 
# mayor (>) ,mayor o igual(>=) , menor(<) menor o igual(<=), igualdad (==),diferente !=

# ELSE - sino se cumple haga otra cosa 
#ELIF sino (CONDICION) ejecuta la instruccion

# es mayor a 18, si el valor es igual a 17, ya casi soy mayor de de edad, soy bb 

edad = 18

if edad >= 18:
    print("Es mayor de edad")
    print("ya puedo ir a rumbiar solo")
elif edad == 17:
    print("ya casi soy mayor de edad")
else:
    print("soy bb")

print("estoy fuera del if ")

# es mayor a 18, si el valor es igual a 17, ya casi soy mayor de de edad, si es igual 

edad = 15

if edad >= 18:
    print("Es mayor de edad")
    print("ya puedo ir a rumbiar solo")
elif edad == 17:
    print("ya casi soy mayor de edad")
elif edad == 15:
    print("soy un quincianero")
else:
    print("soy bb")
    
print("estoy fuera del if ")