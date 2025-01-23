# Currency Recognition System

A modern web application for real-time recognition of Indian currency notes using computer vision and deep learning. This system is built with Flask and TensorFlow, providing accurate detection along with confidence scoring.

---

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Upload Interface

![Upload Interface](screenshots/upload.png)

### Detection Result

![Detection Result](screenshots/result.png)

---

## ✨ Features

- Real-time detection of Indian currency notes
- Support for multiple image formats (JPG, PNG, WEBP, etc.)
- High accuracy detection with confidence scores
- Modern, responsive web interface
- Drag-and-drop image upload functionality

---

## 🛠 Tech Stack

### Backend

- **Python 3.x**
- **Flask** (web framework)
- **OpenCV** (image processing)
- **TensorFlow** (deep learning)
- **NumPy** (numerical computations)

### Frontend

- **HTML5** & **CSS3**
- **JavaScript**
- **Responsive Design**

---

## 🚀 Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/vishaldhavali/Diploma_currency-recognition-system.git
cd Diploma_currency-recognition-system
```
### 2. Create a Virtual Environment


# For Windows
```bash
python -m venv env
.\env\Scripts\activate
```

# For Linux/Mac
```bash
python -m venv env
source env/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
python index.py
```
### 5. Access the Web Application
Open your browser and visit: http://127.0.0.1:5000

### 🎯 Usage Instructions
1.Access the web interface at http://127.0.0.1:5000.
2.Drag and drop an image or click to upload an image of an Indian currency note.
3.Click the "DETECT" button to process the image.
4.View the results, including the detected currency and its confidence score.
