#operaciones 
#key y valor 
super_heores = {
    "spiderman" : "piter",
    "Batman" : "bruce",
    "Iroman" : "tony"
}
super_heores["spiderman"] = "harry"
print(super_heores)
super_heores["hulk"] = "bruce banner"
print(super_heores)

super_heores.update({"Black panter":"t´challa"})
super_heores.update({"Batman":"bruce wayne"})
print(super_heores)

super_heores.pop("hulk")
print(super_heores)

#recorrer los diccionarios 
for hereo in super_heores:
    print(hereo)

for hereo in super_heores:
    print(super_heores[ hereo])

for value in super_heores.values():
    print(value)

for key in super_heores.keys():
    print(key)

super_hereos2 = super_heores.copy()

super_hereos2["Iroman"] = "jaime"

print(super_heores)
print(super_hereos2)

dc ={
    "Batman":"murcielago",
    "superman":"hierro"
}

marvel ={
    "Spiderman":"hombre araña",
    "Iroman":"hombre de lata"
}

heroes = {
    "dc": dc,
    "marvel": marvel
}

print(heroes)
print(heroes["marvel"]["spiderman"])
print(heroes["dc"]["superman"])