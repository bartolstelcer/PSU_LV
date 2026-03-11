# 1.

print("Radni sati: ")
radni_sati = int(input())
print("€/h: ")
eura_po_satu = float(input())

ukupno = radni_sati * eura_po_satu
print("Ukupno:", ukupno)

# def total_euro(radni_sati, eura_po_satu):
#    return radni_sati * eura_po_satu
# print("Ukupno:", total_euro(35, 8.5))

# 2.

print("Unesite ocjenu (0.0 - 1.0):")
unos = input()

try:
    ocjena = float(unos)
    
    if ocjena < 0.0 or ocjena > 1.0:
        print("Pogresan unos!")

except ValueError: 
    print("Pogresan unos!")

if 1.0 > ocjena >= 0.9:
    print("Ocjena: A")
elif 0.9 > ocjena >= 0.8:
    print("Ocjena: B")
elif 0.8 > ocjena >= 0.7:
    print("Ocjena: C")
elif 0.7 > ocjena >= 0.6:
    print("Ocjena: D")
elif 0.6 > ocjena >= 0.0:
    print("Ocjena: F")

# 3. 

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

# 4.

print("Unesite ime datoteke: ")
datoteka = input()

try:
    fhand = open(datoteka)
    ukupno = 0
    broj_linija = 0
    
    for line in fhand:
        line = (fhand.readline())
        if line.startswith("X-DSPAM-Confidence:"):
            broj_linija = broj_linija + 1
            vrijednost = float(line.split(":")[1].strip())
            ukupno = ukupno + vrijednost
            
    if broj_linija > 0:
        prosjek = ukupno / broj_linija
        print("Ime datoteke:", datoteka)
        print("Average X-DSPAM-Confidence:", prosjek)
                
    elif broj_linija == 0:
        print("Ime datoteke:", datoteka)
        print("Average X-DSPAM-Confidence: ", 0)                
except:
    print("Datoteka ne postoji!")

# 5.

file = open("song.txt")

rijeci = {}

for line in file:
    line = line.strip()
    words = line.split()
    
    for word in words:
        rijeci[word] = rijeci.get(word, 0) + 1

count = 0

for word in rijeci:
    if rijeci[word] == 1:
        print(word)
        count = count + 1

print("Broj riječi:", count)
