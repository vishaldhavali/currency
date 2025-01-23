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

1. Clone the repository:  
   `git clone https://github.com/vishaldhavali/Diploma_currency-recognition-system.git`  
   `cd Diploma_currency-recognition-system`

2. Create a virtual environment:  

   For Windows:  
   `python -m venv env`  
   `.\env\Scripts\activate`  

   For Linux/Mac:  
   `python -m venv env`  
   `source env/bin/activate`

3. Install the required dependencies:  
   `pip install -r requirements.txt`

4. Run the application:  
   `python index.py`

5. Access the web application:  
   Open your browser and visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🎯 Usage Instructions

1. Access the web interface at [http://127.0.0.1:5000](http://127.0.0.1:5000).  
2. Drag and drop an image or click to upload an image of an Indian currency note.  
3. Click the "DETECT" button to process the image.  
4. View the results, including the detected currency and its confidence score.  

---

## 📂 Project Structure

currency-recognition-system/
├── static/                      # Contains static assets like images, CSS, and JavaScript
│   ├── background.jpg           # Background image for the web interface
│   └── upload-icon.png          # Icon for the drag-and-drop upload functionality
├── templates/                   # Contains HTML templates for the Flask app
│   ├── error.html               # Error page template
│   ├── index.html               # Home page template
│   └── result.html              # Results display page template
├── Main.py                      # Core logic for the application
├── DetectChars.py               # Module for character detection
├── DetectPlates.py              # Module for plate detection
├── PossibleChar.py              # Helper module for possible character filtering
├── PossiblePlate.py             # Helper module for possible plate filtering
├── Preprocess.py                # Module for preprocessing input images
├── index.py                     # Entry point for the Flask application
└── requirements.txt             # List of dependencies required for the project



---

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the project.  
2. Create a feature branch: `git checkout -b feature/YourFeature`.  
3. Commit your changes: `git commit -m "Add your message here"`.  
4. Push to the branch: `git push origin feature/YourFeature`.  
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 📞 Contact

Vishal Dhavali  
GitHub: [@vishaldhavali](https://github.com/vishaldhavali)  
Email: vishaldhavali123@gmail.com

---

## 🔖 Acknowledgments

- OpenCV Documentation  
- TensorFlow Documentation  
- Indian Currency Dataset  
- Flask Documentation
