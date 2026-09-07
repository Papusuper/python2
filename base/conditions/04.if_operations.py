# expresion que se evalua y devuelve falso o verdadero 
# IF condicion, si la condicion es verdader, ejecuta las instrucciones que esten debajo del if, sino se 
# mayor (>) ,mayor o igual(>=) , menor(<) menor o igual(<=), igualdad (==),diferente !=

# ELSE - sino se cumple haga otra cosa 
#ELIF sino (CONDICION) ejecuta la instruccion

# es mayor a 18, si el valor es igual a 17, ya casi soy mayor de de edad, soy bb 
#operaciones logicas, nad => es mayor a 17 AND es menor a 25
# OR es mayor a 17 OR tiene permiso, puede ir a la fiesta 

#tablas del AND
#condiction1 condiction2 resultado
#True       True        True
#True       False       False
#False      True        False
#False      False       False

#tabla del OR
#Condicion1 Condiction2 Resultado
#True       True        True
#True       False       True
#False      True        True
#False      False       False

edad = 17

if edad >= 17 and edad <= 25:
    print("listo para ir a la universidad")
else:
    print("estoy en el colegio")

edad = 70

if (edad >= 18 and edad <= 25) or edad >= 70:
    print("listo para ir a la universidad")
else:
    print("estoy en el colegio")

#Si es mayor de edad 18, puede salir, pero si es menor de 17 AND mayor a 15 y tiene permiso, puede ir a rumbiar, si no, quedate en casa  
permiso = True
edad = 18

if edad >= 18 or (edad <= 17 and edad >= 15 and permiso == True):
    print("puede salir a rumbiar")
else:
    print("quedate en casa")
