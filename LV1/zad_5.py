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

print("Broj rijeci:", count)