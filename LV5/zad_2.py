import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

data = pd.read_csv("C:\\Users\\Admin\\Desktop\\Bartol\\pythonProgrami\\LV5\\occupancy_processed.csv")

X_train, X_test, y_train, y_test = train_test_split(data[['S3_Temp', 'S5_CO2']], data['Room_Occupancy_Count'], test_size = 0.2, stratify = data['Room_Occupancy_Count'])

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors = 5)

knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(conf_matrix)

accuracy = accuracy_score(y_test, y_pred)
print("Točnost klasifikacije:", accuracy)

precision = precision_score(y_test, y_pred, average = None)
print("Preciznost po klasama:", precision)

recall = recall_score(y_test, y_pred, average = None)
print("Odziv po klasama:", recall)