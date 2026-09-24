# otra condicion es swith pero es python se llama mach (shell bad)
# la "f" es para poner variables texto
#ejemplo con if
#patter macthing 
day = "saturday"

if day == "saturday" or day == "sunday":
    print(f"{day} is a weekend.")
elif day in ["monday","tuesday","wednesday","thursday","friday"]:
    print(f"{day} is a weekend.")
else:
    print("that's not valid day of teh week ")

day = "saturday"
# la tecla "|" se utliza o funciona como un AND o mejor dicho OR
match day:
    case "saturday" | "sunday":
        print(f"{day} is a weekend.")
    case "monday" | "tuesday" | "wednesday"|"thurday"|"friday":
        print(f"{day} is a weekend.")
    case _:
        print("that's not valid day of teh week")

confing = {"type":"database", "name": "postgreSQL", "version": 13}

#patter macthing 
match confing:
    case{"type": "database", "name":name,"version":version}:
        print(f"datbase{name} (version {version})")
    case {"type":"cache","name": name}:
        print(f"cache system {name}")
    case _:
        print("unknown configuration.")
point = (5,4)
match point:
    case (x,y) if x == y:
        print(f"point is on diagnal at {x} ")
    case (x,y) if x > 0 and y > 0:
        print(f"point {point} is in the first quedrant")
    case (x,y):
        print(f"point {point} is somewhere else")