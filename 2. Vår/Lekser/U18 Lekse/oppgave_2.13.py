todo = []

def lese():
    fil = open("Todo.txt", "r", encoding="utf-8")
    todo = fil.readlines()
    fil.close()
    for objekt in todo:
        print(objekt)

def skrive():
    with open("Todo.txt", "w", encoding="utf-8") as fil:
        fil.writelines(todo)
    

bruker_input = str(input("Hei! Vil du lese eller skrive en todo liste? skriv enten lese eller skrive \n"))

if bruker_input.lower() == "lese": 
    lese()
elif bruker_input.lower() == "skrive":
    bruker_input_2 = int(input("hvor mange elementer vil du ha? Skriv kun et heltall :) \n"))
    for i in range(0, bruker_input_2):
        bruker_input_3 = str(input(f"hva er ditt {i+1} objekt på listen? oppgi som str \n"))
        todo.append(bruker_input_3 +"\n")
    skrive()
else:
    print("Dette funket ikke, vennligst kjør programmet igjen :)")
