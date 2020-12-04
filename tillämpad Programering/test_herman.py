again="y"
areor=[]
antalrektanglar=0
print("Programmet räknar ut ett rätblock med sidorna som du matar in.")
while again=="y":
    areor.append([])
    sida1=int(input("Ange längden för sida 1"))
    areor[antalrektanglar].append(sida1)
    sida2=int(input("Ange längden för sida 2"))
    areor[antalrektanglar].append(sida2)
    höjd=input("Ange hur högt höjden ska beräknas. (Måste vara ett heltal")
    while type(höjd)!=int:
        höjd=input("Ange hur högt höjden ska beräknas. (Måste vara ett heltal")
    if höjd<=0:
        höjd=1
    if höjd>=10:
        höjd=10
    print(f"Arean för basen är {sida1*sida2}ae.")
    if sida1 == sida2:
        print("Basen är en kvadrat")
        areor[antalrektanglar].append("true")
    else:
        print("Basen är inte en kvadrat")
        areor[antalrektanglar].append("false")
    print("Höjden    | Volymen")
    antalrektanglar+=1
    for i in range(1,höjd+1):
        print(f"{i}le       |     {i*sida1*sida2}ve")
    print()
    again=str(input("Vill du göra en uträkning till? (y/n)"))
for u in areor:
    print(f"Sidona är {u[0]} och {u[1]}",end=" ")
    if u[2]=="true":
        print("Rektegeln är en kvadrat")
    else:
        print("Rektageln är inte en kvadrat")
    print()