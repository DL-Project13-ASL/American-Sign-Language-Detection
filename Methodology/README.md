# 🛠️ Methodology

This project follows a complete end-to-end pipeline for building a **real-time ASL Alphabet Recognition System**. The methodology includes dataset handling, landmark extraction, deep-learning model training, evaluation, and real-time prediction.

---

## 🔹 1. Dataset Loading

- The ASL Alphabet Dataset (Kaggle) containing **87,000+ images** across **29 classes** is loaded.
- Each class (A–Z, SPACE, DELETE, NOTHING) is stored in separate folders.
- Steps performed:
  - Scan dataset directories
  - Validate image formats (`.jpg`, `.png`, `.jpeg`)
  - Count images per class
  - Assign labels based on folder names

---

## 🔹 2. Hand Landmark Extraction (MediaPipe Hands)

Instead of using raw images, the system extracts **21 hand landmarks**, each having **(x, y, z)** coordinates.

For every image:
1. Read image and convert BGR → RGB  
2. Use MediaPipe Hands to detect a single hand  
3. Extract all **21 landmarks**  
4. Normalize coordinates by subtracting the wrist point (landmark 0)  
5. Flatten into **63 total features** (21 × 3)

If no hand is detected → image is skipped.

This method is lightweight, robust, and better than raw image training.

---

## 🔹 3. Dataset Construction

After extracting the features:
- A structured DataFrame is created containing:
  - **63 landmark features**
  - **1 label column**
- Column format example:
