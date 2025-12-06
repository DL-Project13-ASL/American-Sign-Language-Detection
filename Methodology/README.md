# 🚀 Methodology: Real-Time ASL Alphabet Recognition

This project follows a structured pipeline to build an American Sign Language (ASL) alphabet recognition system capable of real-time gesture classification. The core approach leverages **MediaPipe** for robust feature extraction and a **Multilayer Perceptron (MLP)** for deep learning classification.

## 1. Dataset Loading and Preparation

The foundation of the project relies on image data representing ASL hand signs.

* [cite_start]**Source:** ASL Alphabet Dataset from Kaggle[cite: 22, 133].
* [cite_start]**Target Classes:** 29 distinct classes, including the letters A-Z and special classes: `SPACE`, `NOTHING`, and `DELETE`[cite: 30, 133].
* [cite_start]**Process:** The dataset directory was scanned, and each image folder's name was assigned as the class label[cite: 134, 135].

## 2. Hand Landmark Extraction (Feature Engineering)

To efficiently train the neural network, raw images were converted into a set of structured, numerical features representing the hand's geometry.

* [cite_start]**Tool:** Google's **MediaPipe Hands** model[cite: 74, 142].
* [cite_start]**Detection:** Detects a single hand and extracts **21 key 3D landmarks** (x, y, z coordinates) per image[cite: 89, 142, 146].
* [cite_start]**Normalization:** All 21 landmarks were normalized by subtracting the coordinates of the **wrist point (landmark 0)**[cite: 91, 147, 148]. [cite_start]This step is crucial for reducing noise from variations in hand position, size, and camera distance[cite: 149, 153].
* [cite_start]**Feature Vector:** Each image was flattened into a vector of **63 numerical features** (21 landmarks $\times$ 3 coordinates)[cite: 92, 152].
* [cite_start]**Output:** The processed data was combined into a Pandas DataFrame and saved as `asl_landmarks.pkl`[cite: 99, 155, 160].

## 3. Data Preprocessing for Model Training

The prepared dataset was transformed into a format suitable for the MLP classifier.

* [cite_start]**Label Encoding:** The string labels (e.g., 'A', 'B') were converted into corresponding integers using a `LabelEncoder` (e.g., $A \rightarrow 0, B \rightarrow 1$)[cite: 162, 163, 164].
* [cite_start]**Train-Test Split:** The dataset was split into **80% training** and **20% testing** subsets, using **stratification** to ensure proportional class representation in both splits[cite: 105, 106, 167, 168, 169].
* [cite_start]**Feature Scaling:** The features were standardized using **`StandardScaler`** to have a mean of 0 and a variance of 1. This is critical for improving the performance and stability of the neural network[cite: 171, 174]. [cite_start]The scaler was fit on the training data and then used to transform both training and test data[cite: 172, 173].

## 4. Model Building (MLP Classifier)

A Multilayer Perceptron (MLP) was constructed using TensorFlow/Keras for the multi-class classification task.

* [cite_start]**Architecture (Dense Layers):** $\text{Input} \rightarrow 256 \rightarrow 128 \rightarrow 64 \rightarrow \text{Output (29 classes)}$[cite: 110, 111, 179].
* **Key Components:**
    * [cite_start]**Activation:** ReLU for non-linearity[cite: 180].
    * [cite_start]**Regularization:** Batch Normalization and Dropout layers were included to improve stability and reduce overfitting[cite: 181, 182].
    * [cite_start]**Output Layer:** Softmax activation for the final 29-class classification[cite: 183].
* **Compilation:**
    * [cite_start]**Optimizer:** Adam (with a learning rate of $0.001$)[cite: 113, 185, 186].
    * [cite_start]**Loss Function:** `sparse_categorical_crossentropy`[cite: 114, 187].
    * [cite_start]**Metric:** Accuracy[cite: 188].
* [cite_start]**Training Callbacks:** `EarlyStopping`, `ReduceLROnPlateau`, and `ModelCheckpoint` were configured to manage the training process and save the best-performing model weights[cite: 115, 116, 117, 118, 189].

## 5. Real-Time Detection and Deployment

The trained model was deployed to function as a live ASL recognition system.

* [cite_start]**Artifact Saving:** The following components were saved for inference[cite: 212]:
    1.  [cite_start]`asl_model.h5` (Trained MLP model) [cite: 129, 213]
    2.  [cite_start]`scaler.pkl` (Feature scaler) [cite: 131, 214]
    3.  [cite_start]`label_encoder.pkl` (Class mapping) [cite: 130, 215]
* **Live Prediction Pipeline:**
    1.  [cite_start]Webcam frames are captured using **OpenCV**[cite: 219].
    2.  [cite_start]**MediaPipe** extracts the hand landmarks on each frame[cite: 220].
    3.  [cite_start]Landmarks are normalized and scaled using the saved `scaler.pkl`[cite: 221].
    4.  [cite_start]The trained model (`asl_model.h5`) predicts the ASL class[cite: 222].
    5.  [cite_start]The prediction is displayed live on the video feed[cite: 223].

---
