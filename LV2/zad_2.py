import numpy as np
import matplotlib.pyplot as plt

# a)

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1, 2, 3, 4, 5, 6), delimiter = ",", skiprows = 1)

# b)

plt.scatter(data[:, 1], data[:, 0], label='mpg vs. hp')

# c) 

plt.scatter(data[:, 1], data[:, 0], s = data[:, 5] * 10, alpha = 0.5, label = 'mpg vs. hp & wt')

plt.xlabel('Konjske snage')
plt.ylabel('Potrosnja goriva')
plt.title('Ovisnost potrosnje automobila o konjskim snagama')
plt.show()

# d)

mpgVrijednosti = data[:, 0]
minVrijednosti = np.min(mpgVrijednosti)
maxVrijednosti = np.max(mpgVrijednosti)
meanVrijednosti = np.mean(mpgVrijednosti)
print("Minimalna potrosnja:", minVrijednosti)
print("Maksimalna potrosnja:", maxVrijednosti)
print("Srednja potrosnja:", meanVrijednosti)

# e)

cilindar6 = data[data[:, 3] == 6]
mpgVrijednosti6 = cilindar6[:, 0]
minVrijednosti6 = np.min(mpgVrijednosti6)
maxVrijednosti6 = np.max(mpgVrijednosti6)
meanVrijednosti6 = np.mean(mpgVrijednosti6)
print("Minimalna potrosnja:", minVrijednosti6)
print("Maksimalna potrosnja:", maxVrijednosti6)
print("Srednja potrosnja:", meanVrijednosti6)