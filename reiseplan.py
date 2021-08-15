print("Hei! Velkommen til din reiseplanlegger!. Først vil jeg spørre deg om 5 reisemål\n")
steder = []
for x in range(5):
    sted = input("Skriv et reisemål:\n")
    steder.append(sted)

print("Så vil jeg spørre deg om 5 klesplagg\n")
klesplagg = []
for x in range(5):
    plagg = input("Skriv et klesplagg:\n")
    klesplagg.append(plagg)

print("Så vil jeg spørre deg om 5 avreisedatoer\n")
avreisedatoer = []
for x in range(5):
    dato = input("Skriv en dato:\n")
    avreisedatoer.append(dato)

reiseplan = []
reiseplan.extend([steder, klesplagg, avreisedatoer])
for a in reiseplan:
    print(a)

#Skriver ut elementet på oppgitt plass.
i1 = int(input("Gi meg et heltall:\n"))
i2 = int(input("Gi meg et annet heltall:\n"))
if (i1 >= 0 and i1 < len(reiseplan)) and (i2 >= 0 and i2 < len(reiseplan[i1])):
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input")
