import cv2
import mediapipe as mp
import numpy as np
import pickle
import tensorflow as tf


MODEL_PATH = "asl_model.h5"
SCALER_PATH = "scaler.pkl"
ENCODER_PATH = "label_encoder.pkl"

print(" Loading model and preprocessors...")
model = tf.keras.models.load_model(MODEL_PATH)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

print(" Model, scaler, and label encoder loaded!")


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def extract_hand_landmarks_from_frame(frame_bgr):
    """
    Input: BGR frame from OpenCV
    Output: list of 63 features (21 landmarks * 3) or None
    """
    img_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        wrist = hand_landmarks.landmark[0]

        flat_landmarks = []
        for lm in hand_landmarks.landmark:
            flat_landmarks.append(lm.x - wrist.x)
            flat_landmarks.append(lm.y - wrist.y)
            flat_landmarks.append(lm.z - wrist.z)

        return flat_landmarks, hand_landmarks
    return None, None


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Could not open webcam.")
    exit()

print(" Starting real-time ASL detection... (Press 'q' to quit)")

while True:
    ret, frame = cap.read()
    if not ret:
        print(" Failed to grab frame.")
        break


    frame = cv2.flip(frame, 1)


    features, hand_landmarks = extract_hand_landmarks_from_frame(frame)

    label_text = "No hand detected"
    color = (0, 0, 255)

    if features is not None:

        X = np.array(features).reshape(1, -1)
        X_scaled = scaler.transform(X)


        preds = model.predict(X_scaled, verbose=0)
        class_id = np.argmax(preds, axis=1)[0]
        class_label = label_encoder.inverse_transform([class_id])[0]
        confidence = float(np.max(preds))

        label_text = f"{class_label} ({confidence*100:.1f}%)"
        color = (0, 255, 0)


        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )


    cv2.putText(
        frame,
        label_text,
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        color,
        2,
        cv2.LINE_AA
    )

    cv2.imshow("ASL Real-Time Detection", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
hands.close()
cv2.destroyAllWindows()
print(" Exited.")
