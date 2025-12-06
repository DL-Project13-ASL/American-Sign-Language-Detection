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
- Column format example: label, x0, y0, z0, x1, y1, z1, ... x20, y20, z20
- Dataset saved as: asl_landmarks.pkl
  
---

## 🔹 4. Label Encoding

The labels (A–Z, space, delete, nothing) are converted to numeric form using **LabelEncoder**.

Example:
- A → 0  
- B → 1  
- C → 2  
- …  

This is required for deep learning model training.

---

## 🔹 5. Train–Test Split

The dataset is divided as:
- **80% Training**
- **20% Testing**

Stratification ensures each class is evenly represented in both splits.

---

## 🔹 6. Feature Scaling

Deep learning models perform better with normalized inputs.

- `StandardScaler` is applied:
- `fit_transform()` on training data
- `transform()` on test data

All 63 features are standardized to mean = 0 and variance = 1.

---

## 🔹 7. Model Building (MLP Classifier – TensorFlow/Keras)

A **Multilayer Perceptron** is built for gesture classification.

### Architecture:
- Dense(256) → ReLU → BatchNorm → Dropout  
- Dense(128) → ReLU → BatchNorm → Dropout  
- Dense(64) → ReLU → BatchNorm → Dropout  
- Output Layer (Softmax, 29 classes)

### Model settings:
- Optimizer: **Adam (lr=0.001)**
- Loss: **sparse_categorical_crossentropy**
- Metric: **accuracy**

### Callbacks used:
- EarlyStopping  
- ReduceLROnPlateau  
- ModelCheckpoint  

---

## 🔹 8. Model Training

The MLP model is trained with:
- Epochs: up to **100**
- Batch size: **128**
- Validation on test split
- Automatic LR reduction when validation loss plateaus

The best model is saved as: asl_model.h5

---

## 🔹 9. Model Evaluation

After training, the model is evaluated on the 20% test set.

Metrics:
- **Training Accuracy:** 99.78%
- **Testing Accuracy:** 99.53%
- **Training Loss:** very low  
- **Testing Loss:** very low

Additional outputs:
- Confusion Matrix  
- Classification Report  
- Accuracy/Loss training curves  

The model shows excellent generalization with minimal overfitting.

---

## 🔹 10. Saving Final Components

To support real-time use, the following are saved:

| File | Purpose |
|------|---------|
| `asl_model.h5` | Trained MLP model |
| `scaler.pkl` | StandardScaler object |
| `label_encoder.pkl` | Label mappings (A–Z, space, delete, nothing) |

---

## 🔹 11. Real-Time Gesture Detection

Using webcam + MediaPipe:
1. Capture live frames  
2. Detect hand landmarks in each frame  
3. Normalize & scale landmarks  
4. Predict using trained model  
5. Display predicted ASL letter on screen  

This completes the real-time ASL alphabet recognition system.

---


