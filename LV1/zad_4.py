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