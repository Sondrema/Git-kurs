#Programmere et system som lar bruker holde styr på, legge til og skrive ut venners bursdager.

bursdager = {"andreas":"2.februar"}
def utskrift():
    print(bursdager)
def legge_til(x,y):
    bursdager[x] = y
def fjerne(a):
    del bursdager[a]

svar = input("Hei, velkommen til din venneoversikt!. Hva ønsker du å gjøre?\n")
if svar.lower() == "legge til bursdag":
    hvem = input("Hvem ønsker du å legge til?\n")
    når = input("Når har personen bursdag?\n")
    legge_til(hvem, når)
    print("Lagrede bursdager er nå:", bursdager)
elif svar.lower() == "fjerne bursdag":
    hvem2 = input("Hvem ønsker du å fjerne fra listen?\n")
    fjerne(hvem2)
    print("Lagrede bursdager er nå:", bursdager)
elif svar.lower() == "oversikt over bursdager":
    utskrift()
else:
    print("Det forstod jeg ikke. Jeg har tre valg: 1)legge til bursdag 2)fjerne bursdag eller 3)oversikt over bursdager.")
