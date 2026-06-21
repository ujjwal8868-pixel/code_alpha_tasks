
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
heart_data = pd.read_csv("heart.csv")

# Display first rows
print(heart_data.head())

# Dataset info
print(heart_data.info())

# Check missing values
print(heart_data.isnull().sum())

# Statistical summary
print(heart_data.describe())

# Target distribution
print(heart_data['target'].value_counts())

# Splitting features and target
X = heart_data.drop('target', axis=1)
Y = heart_data['target']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# Model training
model = LogisticRegression(max_iter=3000)
model.fit(X_train, Y_train)

# Training accuracy
train_pred = model.predict(X_train)
train_acc = accuracy_score(train_pred, Y_train)
print("Training Accuracy:", train_acc)

# Testing accuracy
test_pred = model.predict(X_test)
test_acc = accuracy_score(test_pred, Y_test)
print("Testing Accuracy:", test_acc)

# ---------------- Prediction ----------------

input_data = (59, 1, 2, 126, 218, 1, 1, 134, 0, 2.2, 1, 1, 1)

input_data = pd.DataFrame([input_data], columns=X.columns)
prediction = model.predict(input_data)

print("Prediction:", prediction)

if prediction[0] == 0:
    print("The person does NOT have heart disease")
else:
    print("The person HAS heart disease")