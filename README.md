# ✋🧠 American Sign Language (ASL) Alphabet Recognition  
### Deep Learning & Applications (UEC642) — Final Project

---

## 🌟 Introduction

Welcome to the **ASL Alphabet Recognition System**, a complete deep-learning project developed as part of the **Deep Learning & Applications – UEC642** course.

This repository is submitted to  
**Dr. Gaganpreet Kaur**  

Submitted by:  
- **Ishmit Singh — 102215056**  
- **Adamya Sharma — 102215132**  
- **Sumedha Khosla — 102395002**

This project explores how **MediaPipe**, **Deep Learning**, and **Computer Vision** can be combined to recognize **American Sign Language (ASL)** alphabet gestures with remarkable accuracy. The goal is to create an efficient, lightweight, and real-time gesture recognition system that can serve as a stepping stone toward more advanced sign language translation and accessibility tools.

---

## 📌 Overview of the Repository

This repository contains all components required for the complete ASL recognition pipeline:

### 🔹 **Methodology**
A detailed explanation of how the dataset is processed, how MediaPipe extracts hand landmarks, how the model is trained, and how real-time detection is achieved.

### 🔹 **Flowcharts**
Clear visual diagrams that represent each stage in the methodology — from dataset loading to final model deployment.

### 🔹 **Results**
Performance evaluation including confusion matrix, training history plots, and real-time gesture detection screenshots demonstrating high classification accuracy.

### 🔹 **Model & Code**
All essential files for model inference and real-time ASL detection, including:
- Trained models (`asl_model.h5`, `best_asl_model.h5`)
- Preprocessing tools (`label_encoder.pkl`, `scaler.pkl`)
- Real-time detection script (`live.py`)
- Full training notebook (`signnnn.ipynb`)

### 🔹 **Project Report**
A comprehensive PDF report detailing every stage of the project including methodology, architecture, results, literature survey, and conclusion.

---

## 🧠 Project Summary

The ASL recognition system is built using:
- **MediaPipe Hands** for extracting 21 hand landmarks  
- **Multilayer Perceptron (MLP)** for classification  
- **StandardScaler + LabelEncoder** for preprocessing  
- **OpenCV** for real-time webcam detection  

The system achieves:
- **99.53% Testing Accuracy**  
- Smooth real-time detection  
- High precision & recall across 29 ASL classes  

This demonstrates the effectiveness of landmark-based feature extraction in gesture classification, offering a computationally lightweight alternative to CNN-based image models.

---

## 💡 Purpose & Motivation

Millions of individuals worldwide rely on sign languages for communication. However, barriers often exist between signers and non-signers.  
Our aim was to explore how modern AI techniques can:

- Promote accessibility & inclusive communication  
- Enable real-time visual interpretation  
- Provide a foundation for more advanced tools such as sentence-level recognition  

This project highlights the potential of deep learning to bridge communication gaps through innovative, impactful, and practical solutions.

---

## 📁 Repository Structure

ASL-Recognition/
│── code/
│── methodology/
│── flowcharts/
│── results/
│── project-report/
│── README.md (this file)


---

## 🌐 Final Note

Thank you for exploring our ASL Alphabet Recognition project!  
We hope this repository provides value to researchers, students, and developers interested in deep learning–powered accessibility tools.


---
