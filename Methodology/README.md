# 🧪 Methodology

This project follows a structured machine-learning workflow to build and deploy a real-time American Sign Language (ASL) recognition system using deep learning and MediaPipe.

---

### 1️⃣ Dataset Loading

The ASL Alphabet dataset from Kaggle was used, containing labeled gesture images across 29 different classes (A–Z, SPACE, DELETE, NOTHING). The dataset was scanned class-wise, and file integrity checks were performed before processing.

---

### 2️⃣ Hand Landmark Extraction (MediaPipe)

Instead of using full raw image data, hand geometry was extracted using **MediaPipe Hands**:

- Each sample generates **21 landmark points**
- Each point provides **x, y, z coordinates**
- Resulting feature vector size → **63 values per image**

Landmarks were normalized relative to the wrist joint to reduce variations from hand distance and camera positioning.

---

### 3️⃣ Dataset Construction

Extracted numeric features were stored in a structured DataFrame with the following format:


