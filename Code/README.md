# 🧩 Code Section – ASL Recognition System

This folder contains all the essential source code files, trained model artifacts, preprocessing tools, and notebooks required to run, evaluate, and deploy the ASL Alphabet Recognition System.

Each file in this section plays a specific role in enabling the full workflow from model loading to real-time gesture detection.

---

## 📁 Files Included

### 🔹 1. `asl_model.h5`
This is the **trained Multilayer Perceptron (MLP) model** used for ASL alphabet classification.  
It was trained on 63-dimensional landmark features extracted from MediaPipe.

Contains:
- Final model architecture  
- Learned weights  
- Supports 29 output classes (A–Z, space, delete, nothing)

---

### 🔹 2. `best_asl_model.h5`
This file stores the **best-performing version** of the model during training.  
It was saved using **ModelCheckpoint**, based on best validation accuracy.

Use this if you want the most optimized inference model.

---

### 🔹 3. `label_encoder.pkl`
This file contains the **LabelEncoder object** used during preprocessing.  

Purpose:
- Converts numerical predictions (0–28) back to ASL labels (A–Z, space, delete, nothing).
- Ensures consistent mapping during both training and real-time detection.

---

### 🔹 4. `scaler.pkl`
This file includes the **StandardScaler** used for feature normalization.  

Purpose:
- Normalizes all 63 features to mean=0 and variance=1  
- Ensures incoming real-time data matches the scale used during training  
- Required for consistent model inference

---

### 🔹 5. `live.py`
This script runs the **real-time ASL detection system** using:
- OpenCV (webcam feed)
- MediaPipe Hands (landmark extraction)
- Loaded MLP model (prediction)
- Scaler and label encoder (preprocessing/postprocessing)

Features:
- Captures frames from webcam  
- Extracts 21 hand landmarks  
- Normalizes and scales features  
- Predicts ASL alphabet with confidence  
- Displays landmarks + predicted class live on screen  

Run using:
```bash
python live.py

