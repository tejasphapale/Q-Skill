# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# ---------------------------------
# Load Dataset
# ---------------------------------

df = pd.read_csv("Housing.csv")

print("="*60)
print("First Five Records")
print("="*60)

print(df.head())

# ---------------------------------
# Dataset Information
# ---------------------------------

print("\nDataset Information")

print(df.info())

# ---------------------------------
# Check Missing Values
# ---------------------------------

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------
# Convert Categorical Data
# ---------------------------------

encoder = LabelEncoder()

categorical_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
    "furnishingstatus"
]

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

# ---------------------------------
# Features and Target
# ---------------------------------

X = df.drop("price", axis=1)

y = df["price"]

# ---------------------------------
# Split Dataset
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ---------------------------------
# Train Linear Regression Model
# ---------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ---------------------------------
# Prediction
# ---------------------------------

predictions = model.predict(X_test)

# ---------------------------------
# Evaluation
# ---------------------------------

print("\nModel Evaluation")

print("Mean Absolute Error")

print(mean_absolute_error(y_test, predictions))

print("\nMean Squared Error")

print(mean_squared_error(y_test, predictions))

print("\nR2 Score")

print(r2_score(y_test, predictions))

# ---------------------------------
# Actual vs Predicted
# ---------------------------------

comparison = pd.DataFrame({

    "Actual Price": y_test,

    "Predicted Price": predictions

})

print("\nActual vs Predicted")

print(comparison.head(10))

# ---------------------------------
# Scatter Plot
# ---------------------------------

plt.figure(figsize=(8,6))

plt.scatter(y_test, predictions)

plt.xlabel("Actual Price")

plt.ylabel("Predicted Price")

plt.title("Actual Price vs Predicted Price")

plt.grid(True)

plt.show()

# ---------------------------------
# Feature Importance
# ---------------------------------

coefficients = pd.DataFrame({

    "Feature": X.columns,

    "Coefficient": model.coef_

})

print("\nFeature Importance")

print(coefficients)

# ---------------------------------
# Bar Chart
# ---------------------------------

plt.figure(figsize=(10,5))

plt.bar(coefficients["Feature"], coefficients["Coefficient"])

plt.xticks(rotation=90)

plt.title("Feature Importance")

plt.tight_layout()

plt.show()

print("\nProgram Executed Successfully")