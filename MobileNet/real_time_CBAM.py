# -*- coding: utf-8 -*-
"""Real_Time.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1egFXw35SRpwJ9BG4iaflU9vS8UyDV-J4
"""

import os
import cv2
import numpy as np
import tensorflow as tf
from mtcnn import MTCNN

# Load custom model
model_path = "C:/Users/Jaswa/Desktop/Grad Class Folder/CmPE258/Project/mobilenet_cbam_best.h5"
custom_model = tf.keras.models.load_model(model_path)

# model input size and classes for mapping results
classes = ["surprise", "sad", "neutral", "happy", "fear", "disgust", "angry"]
INPUT_SIZE = (224, 224)

# Initialize the face detector
detector = MTCNN()

# Start the webcam feed
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the captured frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    detections = detector.detect_faces(frame_rgb)
    for detection in detections:
        x, y, width, height = detection['box']
        face_img = frame_rgb[y:y+height, x:x+width]
        resized_face = cv2.resize(face_img, INPUT_SIZE)
        resized_face = np.expand_dims(resized_face, axis=0)  # Model input expects a batch of images

        # Predict emotion
        emotion_pred = custom_model.predict(resized_face)
        emotion_label = classes[np.argmax(emotion_pred)]

        # Draw the detected face and write the emotion
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Check if window closed
    if cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Exit upon pressing q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
