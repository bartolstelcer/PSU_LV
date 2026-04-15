import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Učitavanje podataka
data = pd.read_csv("C:\\Users\\Admin\\Desktop\\Bartol\\pythonProgrami\\LV5\\occupancy_processed.csv")

# Podijela podataka na skup za učenje i skup za testiranje (omjer 80%-20%)
X_train, X_test, y_train, y_test = train_test_split(data[['S3_Temp', 'S5_CO2']], data['Room_Occupancy_Count'], test_size = 0.2, stratify = data['Room_Occupancy_Count'])

# Inicijalizacija StandardScaler-a i skaliranje ulaznih veličina
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicijalizacija klasifikatora KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)

# Treniranje modela na skupu za učenje
knn.fit(X_train_scaled, y_train)

# Predikcija na skupu za testiranje
y_pred = knn.predict(X_test_scaled)

# Prikaz matrice zabune
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(conf_matrix)

# Izračun točnosti klasifikacije
accuracy = accuracy_score(y_test, y_pred)
print("Točnost klasifikacije:", accuracy)

# Izračun preciznosti po klasama
precision = precision_score(y_test, y_pred, average = None)
print("Preciznost po klasama:", precision)

# Izračun odziva po klasama
recall = recall_score(y_test, y_pred, average = None)
print("Odziv po klasama:", recall)