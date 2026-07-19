
# ✍️ Handwritten Character Recognition using CNN

## 📌 Project Overview

This project implements a **Handwritten Character Recognition System** using **Convolutional Neural Networks (CNNs)**. The model is trained to recognize handwritten digits (0–9) from images using the **MNIST dataset**. The project can be extended to recognize handwritten alphabets using the **EMNIST dataset** and full words or sentences using sequence models such as **CRNN (Convolutional Recurrent Neural Network)**.

---

## 🎯 Objective

The objective of this project is to:

- Recognize handwritten digits from images.
- Learn image preprocessing techniques.
- Build and train a CNN model.
- Predict handwritten characters with high accuracy.
- Understand the basics of Optical Character Recognition (OCR).

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

---

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/HandwrittenCharacterRecognition.git
```

Move into the project folder:

```bash
cd Handwritten_Character_Recognition
```

Install dependencies:

```bash
pip install tensorflow numpy matplotlib
```

---

## ▶️ Run the Project

### Train the Model

```bash
python train.py
```

### Predict a Digit

```bash
python predict.py

---

## 🔄 Project Workflow

```
Input Image
      │
      ▼
Image Preprocessing
      │
      ▼
CNN Feature Extraction
      │
      ▼
Classification
      │
      ▼
Predicted Digit
```

---

## 📊 Results

- Training Accuracy: **~99%**
- Testing Accuracy: **~98–99%**

*(Accuracy may vary depending on the number of training epochs and system configuration.)*

---
## 📷 Sample Output

```
Input Image:
  [Handwritten Digit]

Predicted Digit: 7

Confidence: 99.2%
```
