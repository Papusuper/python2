#key y valor 
super_heores = {
    "spiderman" : "piter",
    "Batman" : "bruce",
    "Iroman" : "tony"
}

print(super_heores)
print(super_heores["spiderman"])
print(super_heores.get("Batman"))
#solo los key 
print(super_heores.keys())
#solo se cogen valores 
print(super_heores.values())
# se devuleve en tuplas 
print(super_heores.items())

if "Iroman" in super_heores:
    print("Es un heroe de marver")
else:
    print("ese no es de marver busca en dc")
