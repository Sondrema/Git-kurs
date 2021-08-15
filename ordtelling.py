def antall_bokstaver(x):
    return len(x)

def sortering(y):
    liste_ord = y.split()
    ordbok = {}
    for e in liste_ord:
        if e in ordbok:
            ordbok[e] += 1
            print("Ordet", e, "forekommer", ordbok[e], "ganger, og har", antall_bokstaver(e), "bokstaver")
        else:
            ordbok[e] = 1
            print("Ordet", e, "forekommer", ordbok[e], "ganger, og har", antall_bokstaver(e), "bokstaver")

setning = input("Skriv en setning: \n")
liste1 = setning.split()
print("Det er", len(liste1), "ord i setningen din.")
sortering(setning)
