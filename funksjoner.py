#Oppgave 1.1
def adder(tall1, tall2):
    tall3 = tall1 + tall2
    return tall3
print("Summen er:", adder(4,6))
print("Summen er:", adder(19,17))

#Oppgave 1.2 og 1.3
def tellForekomst(minTekst, minBokstav):
    teller = 0
    for x in minTekst:
        if x == minBokstav:
            teller += 1
    return teller
setning = input("Skriv en kort setning: \n")
bokstav = input("Skriv nå en vilkårlig valgt bokstav: \n")
print("Bokstaven", bokstav, "forekommer", tellForekomst(setning, bokstav), "ganger i setningen du skrev.")
