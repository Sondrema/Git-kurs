tall = int(input("Tast inn et tall\n"))
liste = []
minSum = 0
while tall != 0:
    liste.append(tall)
    tall = int(input("Tast inn et tall\n"))

#Printer ut alle elementene
for x in liste:
    print(x)

#Printer ut minSum
for a in liste:
    minSum += a
print("Summen av tallene i listen er:", minSum)

#Printer ut minste element
minste = liste[0]
for b in range(len(liste)):
    if liste[b] < minste:
        minste = liste[b]
print("Det minste tallet i listen er:", minste)

#printer ut største element
storste = liste[0]
for b in range(len(liste)):
    if liste[b] > storste:
        storste = liste[b]
print("Det storste tallet i listen er:", storste)
