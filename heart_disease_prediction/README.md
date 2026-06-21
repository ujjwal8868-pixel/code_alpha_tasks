# ❤️ Heart Disease Prediction using Logistic Regression

## 📌 Project Overview

This project is a **Heart Disease Prediction System** built using **Machine Learning (Logistic Regression)** in **Python (VS Code)**.
It predicts whether a person is likely to have heart disease based on medical attributes such as age, cholesterol, blood pressure, and other health indicators.

---

## 🚀 Features

* Load and analyze heart disease dataset
* Data preprocessing using Pandas
* Train-test split for model evaluation
* Logistic Regression model training
* Model performance evaluation (accuracy score)
* Prediction system for new patient data
* Clean and structured ML pipeline

---

## 🛠️ Technologies Used

* Python 🐍
* Visual Studio Code (VS Code)
* NumPy
* Pandas
* Scikit-learn

---

## 📂 Dataset Information

The dataset contains **13 medical features**:

* age
* sex
* chest pain type (cp)
* resting blood pressure (trestbps)
* cholesterol (chol)
* fasting blood sugar (fbs)
* resting ECG (restecg)
* max heart rate (thalach)
* exercise induced angina (exang)
* oldpeak
* slope
* number of major vessels (ca)
* thal

### 🎯 Target Column

* **0 → No Heart Disease**
* **1 → Heart Disease**

---

## 🤖 Machine Learning Model

* Algorithm: Logistic Regression
* max_iter: 3000
* Train-Test Split: 80% training / 20% testing
* Stratified sampling used for balanced data

---

## 📊 Model Performance

* Training Accuracy: ~85%
* Testing Accuracy: ~80%

---

## 🧪 Sample Prediction

### Input:

```
(59, 1, 2, 126, 218, 1, 1, 134, 0, 2.2, 1, 1, 1)
```

### Output:

```
Prediction: 0
The person does NOT have heart disease
```

---

## ⚙️ How to Run

1. Clone this repository

```bash
git clone <repo-link>
```

2. Install dependencies

```bash
pip install numpy pandas scikit-learn
```

3. Run the project

```bash
python heart_disease_prediction.py
```

---

## 🔮 Future Improvements

* Add feature scaling for better accuracy
* Try advanced models (Random Forest, XGBoost)
* Build a web app using Flask or Streamlit
* Deploy project online for real-time prediction

---

## 👨‍💻 Author

**Ujjwal Srivastava**

B.Tech CSE Student | Machine Learning Enthusiast

---
