import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
import os

# Ensure model folder exists
if not os.path.exists("model"):
    os.makedirs("model")

# Load dataset
data = pd.read_csv("data/phone_prices.csv")

# Encode brand
le = LabelEncoder()
data['brand_encoded'] = le.fit_transform(data['brand'])

# Features & target
X = data[['brand_encoded', 'ram', 'storage', 'battery', 'main_camera', 'front_camera', 'original_price', 'years_of_use']]
y = data['resale_price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
avg_resale = y_test.mean()

# Accuracy percentage approximation
accuracy_percent = (1 - (mae / avg_resale)) * 100

print(f"✅ Model trained successfully!")
print(f"R² Score: {r2:.3f} ({r2*100:.2f}%)")
print(f"Mean Absolute Error: ₹{mae:.2f}")
print(f"Approximate Model Prediction Accuracy: {accuracy_percent:.2f}%")

# Save model
with open("model/phone_resale_model.pkl", "wb") as f:
    pickle.dump((model, le), f)
print("✅ Model saved at model/phone_resale_model.pkl")
