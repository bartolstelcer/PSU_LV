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