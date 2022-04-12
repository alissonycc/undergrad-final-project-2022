import cv2
import sys
import datetime as dt
from time import sleep
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import img_to_array
import numpy as np
import os


def label(predicted):
    if predicted == 0:
        return "Angry"
    elif predicted == 1:
        return "Disgust"
    elif predicted == 2:
        return "Fear"
    elif predicted == 3:
        return "Happy"
    elif predicted == 4:
        return "Sad"
    elif predicted == 5:
        return "Surprise"
    elif predicted == 6:
        return "Neutral"


def biggest_face(faces):
    current = 0
    retorno = []
    for (x, y, z, w) in faces:
        total = x + y + z + w
        if total > current:
            current = total
            retorno = [x, y, z, w]
    return retorno


cur_path = os.path.dirname(__file__)
new_path = os.path.relpath("..\\", cur_path)

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
video_capture = cv2.VideoCapture(0)

model = keras.models.load_model("model.h5")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    face = biggest_face(faces)
    # for (x, y, w, h) in face:
    if face:
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        img = frame[y : y + h, x : x + w]

        img = cv2.resize(img, (48, 48))

        img = img_to_array(img)
        img = img.reshape((1, 48, 48, 3))
        pred = model.predict(img)
        predicted = np.argmax(pred)
        labelOutput = label(predicted)

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 30)
        fontScale = 1
        fontColor = (0, 255, 0)
        thickness = 2
        lineType = 2

        cv2.putText(
            frame,
            labelOutput,
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            thickness,
            lineType,
        )

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
