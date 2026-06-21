# 💳 Credit Scoring Model using Random Forest

## 📌 Project Overview

This project is a **Credit Scoring Model** developed using **Python in Google Colab**. It applies the **Random Forest Machine Learning algorithm** to predict credit risk based on customer financial information.

The model uses a synthetic dataset generated using Scikit-learn's `make_classification()` function containing **1000 records** and **10 financial features**.

---

## 🚀 Features

* Synthetic credit dataset generation
* Data analysis and preprocessing using Pandas
* Train-test dataset splitting
* Random Forest model training
* Credit risk prediction
* Model evaluation using multiple performance metrics
* Confusion Matrix visualization
* Feature Importance analysis

---

## 🛠️ Technologies & Tools Used

* Python 🐍
* Google Colab
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

## 📊 Dataset Information

The dataset includes the following features:

* Income
* Debt
* Payment History
* Credit Age
* Number of Accounts
* Missed Payments
* Credit Limit
* Loan Amount
* Employment Years
* Monthly Expenses

### Target Variable

* **0** → Low Credit Risk
* **1** → High Credit Risk

---

## 🤖 Machine Learning Model

**Algorithm Used:** Random Forest Classifier

### Model Configuration

* Number of Decision Trees: 100
* Random State: 42

### Data Split

* Training Data: 80%
* Testing Data: 20%

---

## 📈 Model Performance

The model achieved the following results:

* Accuracy: **94.5%**
* Precision: **93.26%**
* Recall: **94.31%**
* F1 Score: **93.79%**
* ROC-AUC Score: **94.48%**

---

## 📉 Visualizations

The project provides:

* Confusion Matrix Heatmap
* Feature Importance Graph
---

## ⚙️ How to Run the Project

1. Open the `.ipynb` notebook in Google Colab.
2. Install the required libraries (if needed).
3. Run all cells sequentially.
4. View model performance and visualizations.

---

## 🔮 Future Improvements

* Use real-world credit datasets for more realistic predictions
* Perform hyperparameter tuning to improve model performance
* Compare Random Forest with other machine learning models
* Deploy the model as a web application using Streamlit or Flask

---

## 👨‍💻 Author

**Ujjwal Srivastava**

B.Tech CSE Student | Machine Learning & Web Development Enthusiast
