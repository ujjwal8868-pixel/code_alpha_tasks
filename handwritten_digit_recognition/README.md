# ✍️ Handwritten Character Recognition using CNN

## 📌 Project Overview

This project is a **Handwritten Character Recognition System** developed using **Python in Visual Studio Code (VS Code)**. It uses a **Convolutional Neural Network (CNN)** to recognize handwritten digits from the **MNIST dataset**.

The CNN model learns patterns from thousands of handwritten digit images and predicts the correct digit (0–9) with high accuracy.

---

## 🚀 Features

* Loading and preprocessing the MNIST handwritten digit dataset
* Image normalization and reshaping for CNN input
* Building a deep learning CNN architecture
* Training the model using TensorFlow/Keras
* Evaluating model performance on test data
* Visualizing training and validation accuracy
* Predicting handwritten digits from test images

---

## 🛠️ Technologies & Tools Used

* Python 🐍
* Visual Studio Code (VS Code)
* TensorFlow
* Keras
* NumPy
* Matplotlib

---

## 📂 Dataset Information

**Dataset:** MNIST Handwritten Digits Dataset

Dataset details:

* 70,000 grayscale images of handwritten digits
* Image size: 28 × 28 pixels
* 60,000 training images
* 10,000 testing images
* 10 classes (digits 0–9)

---

## 🤖 CNN Model Architecture

The model consists of:

* Convolution Layer (32 filters, 3×3 kernel, ReLU activation)
* Max Pooling Layer
* Convolution Layer (64 filters, 3×3 kernel, ReLU activation)
* Max Pooling Layer
* Flatten Layer
* Dense Layer (128 neurons, ReLU activation)
* Dropout Layer (0.5) to reduce overfitting
* Output Layer (10 neurons, Softmax activation)

---

## ⚙️ Model Training

* Optimizer: Adam
* Loss Function: Categorical Cross Entropy
* Epochs: 5
* Batch Size: 64
* Validation Split: 10%

---

## 📊 Model Evaluation

The model is evaluated using the MNIST test dataset and provides the final **test accuracy** after training.

The project also displays:

* Training Accuracy vs Validation Accuracy graph
* Sample handwritten digit predictions with images

---

## ⚙️ Installation & Setup

1. Clone the repository:

git clone <repository-link>

2. Install required libraries:

pip install tensorflow numpy matplotlib

3. Run the Python file:

python handwritten_character_recognition.py

---

## 🔮 Future Improvements

* Increase the number of training epochs to improve accuracy
* Add more advanced CNN architectures
* Create a GUI or web application for real-time digit recognition
* Allow users to upload their own handwritten images

---

## 👨‍💻 Author

**Ujjwal Srivastava**

B.Tech CSE Student | Machine Learning & Web Development Enthusiast

