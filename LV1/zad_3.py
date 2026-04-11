brojevi = []

i = 1
while i == 1:
    unos = input("Unesite broj: ")
    if unos == "Done":
        break
    
    try:
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        print("Pogresan unos!")

if brojevi:
    print("Broj unesenih brojeva:", len(brojevi))
    print("Srednja vrijednost:", sum(brojevi) / len(brojevi))
    print("Minimalna vrijednost:", min(brojevi))
    print("Maksimalna vrijednost:", max(brojevi))
    brojevi.sort()
    print("Sortirana lista:", brojevi)