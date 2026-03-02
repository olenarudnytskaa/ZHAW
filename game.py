import random

anzahl_hoelzer = random.randint(10,20) # The game starts with a stack of matches
# (random number: no less than 10, no more than 20).
randomas = anzahl_hoelzer
matches_graphic = '|' * randomas   # symbol

print(f"Anzahl Hoelzer: {anzahl_hoelzer} {matches_graphic}")

spieler_namen = {1: "Computer", 2: "Player"}
start = random.randint(1,2)
print(f"Start: {spieler_namen[start]}")

while anzahl_hoelzer > 0:
    if start == 1:  #computer fangt an
        check = (anzahl_hoelzer - 1) % 4 # computer checkt rest
        if  check > 0 :
            comp_rand = random.randint(1, 3)
            print(f"Die Anzahl der Conputer ist: {check} ")
            anzahl_hoelzer = anzahl_hoelzer - check
        #start = 2
        elif check == 0:
            comp_rand = random.randint(1, 3)
            print(f"Die Anzahl der Conputer ist: {comp_rand}")
            anzahl_hoelzer = anzahl_hoelzer - comp_rand
        start = 2

        print(f"Rest:{anzahl_hoelzer}: {anzahl_hoelzer* '|'} ")
    elif start == 2:
         #player startet
        zahl = (int(input('Geben Sie bitte eine Zahl zwischen 1-3 ein:')))  # immer wieder bei player wiederholt werden
        while zahl < 1 or zahl > 3:
            zahl = (int(input('Geben Sie bitte eine Zahl zwischen 1-3 ein:')))

        anzahl_hoelzer = anzahl_hoelzer - zahl
        print(f"Rest:{anzahl_hoelzer}: {anzahl_hoelzer* '|'}")

        start = 1




if start == 1:
    print("Sorry, you lost")
elif start == 2:
    print("Der Computer hat gewonnen")

