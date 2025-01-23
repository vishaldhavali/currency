from flask import Flask, render_template, request, redirect
import os
from utils import *
from matplotlib import pyplot as plt
import os
from playsound import playsound
import cv2
from PIL import Image
import numpy as np

import subprocess
import gtts
from gtts import gTTS
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_jpg(input_image):
    """Convert any image format to JPG and save as target.jpg"""
    if isinstance(input_image, str):
        # If input is a file path
        img = Image.open(input_image)
    else:
        # If input is a file object
        img = Image.open(input_image)
    
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Save as JPG
    img.save('target.jpg', 'JPEG')
    return 'target.jpg'

def extract_features(image):
    model = ResNet50(weights='imagenet', include_top=False)
    image = cv2.resize(image, (224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    features = model.predict(image)
    return features.flatten()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    number = -1
    note = 200
    confidence = 0
    
    if request.method == "POST":
        if request.files:
            vehicle = request.files["vehicle"]
            
            if not allowed_file(vehicle.filename):
                return render_template("error.html", message="Unsupported file format. Please upload an image file.")
            
            # Save the original uploaded file temporarily
            temp_path = os.path.join('files', vehicle.filename)
            vehicle.save(temp_path)
            
            try:
                convert_to_jpg(temp_path)
                test_img = read_img('files/' + vehicle.filename)
                
                # Your existing image processing code
                original = resize_img(test_img, 0.4)
                display('original', original)

                orb = cv2.ORB_create()
                (kp1, des1) = orb.detectAndCompute(test_img, None)

                training_set = ['files/20.jpg', 'files/50.jpg', 'files/100.jpg', 
                              'files/500.jpg', 'files/2000.jpg', 'files/10.jpg']

                max_val = 8
                max_pt = -1
                max_kp = 0

                for i in range(0, len(training_set)):
                    train_img = cv2.imread(training_set[i])
                    (kp2, des2) = orb.detectAndCompute(train_img, None)

                    bf = cv2.BFMatcher()
                    all_matches = bf.knnMatch(des1, des2, k=2)

                    good = []
                    for (m, n) in all_matches:
                        if m.distance < 0.789 * n.distance:
                            good.append([m])

                    if len(good) > max_val:
                        max_val = len(good)
                        max_pt = i
                        max_kp = kp2

                    print(i, ' ', training_set[i], ' ', len(good))

                if max_val != 8:
                    print(training_set[max_pt])
                    print('good matches ', max_val)
                    train_img = cv2.imread(training_set[max_pt])
                    img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
                    note = str(training_set[max_pt])[6:-4]
                    print('\nDetected denomination: Rs. ', note)
                    
                    # Calculate confidence based on good matches
                    confidence = (max_val / 20) * 100  # Normalize to percentage
                    confidence = min(confidence, 100)  # Cap at 100%
                else:
                    note = "No Matches"
                    confidence = 0
                    print('No Matches')

            except Exception as e:
                print(f"Error processing image: {str(e)}")
                return render_template("error.html", message="Error processing image")
            
            finally:
                # Cleanup: remove temporary files
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                if os.path.exists('target.jpg'):
                    os.remove('target.jpg')

    return render_template("result.html", value=note, confidence=f"{confidence:.1f}")

if __name__ == "__main__":
    # Ensure the files directory exists
    os.makedirs('files', exist_ok=True)
    app.run(debug=True)