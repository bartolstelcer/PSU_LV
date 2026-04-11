import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error

data = pd.read_csv('cars_processed.csv')

data = data.drop(['name'], axis=1)

X = data.drop(['selling_price'], axis=1)
y = data['selling_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

print("Evaluacija na trening skupu:")
print("Mean Absolute Error:", mean_absolute_error(y_train, y_train_pred))
print("R-squared:", r2_score(y_train, y_train_pred))
print("Mean Squared Error:", mean_squared_error(y_train, y_train_pred))
print("Max Error:", max_error(y_train, y_train_pred))

print("\nEvaluacija na testnom skupu:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_test_pred))
print("R-squared:", r2_score(y_test, y_test_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_test_pred))
print("Max Error:", max_error(y_test, y_test_pred))

X_with_dummies = pd.get_dummies(X, drop_first=True)

X_train_dummy, X_test_dummy, y_train_dummy, y_test_dummy = train_test_split(X_with_dummies, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_train_scaled_dummy = scaler.fit_transform(X_train_dummy)
X_test_scaled_dummy = scaler.transform(X_test_dummy)

model_with_dummies = LinearRegression()
model_with_dummies.fit(X_train_scaled_dummy, y_train_dummy)

y_train_pred_dummy = model_with_dummies.predict(X_train_scaled_dummy)
y_test_pred_dummy = model_with_dummies.predict(X_test_scaled_dummy)

print("\nEvaluacija na trening skupu s kategoričkim varijablama:")
print("Mean Absolute Error:", mean_absolute_error(y_train_dummy, y_train_pred_dummy))
print("R-squared:", r2_score(y_train_dummy, y_train_pred_dummy))
print("Mean Squared Error:", mean_squared_error(y_train_dummy, y_train_pred_dummy))
print("Max Error:", max_error(y_train_dummy, y_train_pred_dummy))

print("\nEvaluacija na testnom skupu s kategoričkim varijablama:")
print("Mean Absolute Error:", mean_absolute_error(y_test_dummy, y_test_pred_dummy))
print("R-squared:", r2_score(y_test_dummy, y_test_pred_dummy))
print("Mean Squared Error:", mean_squared_error(y_test_dummy, y_test_pred_dummy))
print("Max Error:", max_error(y_test_dummy, y_test_pred_dummy))