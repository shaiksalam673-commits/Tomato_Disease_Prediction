# 🍅 Tomato Leaf Disease Prediction System

An AI-powered web application that detects and classifies tomato leaf diseases using Deep Learning and TensorFlow. The project provides disease predictions, confidence scores, and treatment recommendations through an interactive Gradio interface.

---

## 📌 Features

- 🔍 Detects multiple tomato leaf diseases
- 🤖 Deep Learning model using TensorFlow/Keras
- 📊 Displays prediction confidence for all classes
- 📸 Supports image upload and webcam input
- 💡 Provides disease descriptions and recommendations
- 🌐 Interactive web interface using Gradio

---

## 🧠 Diseases Supported

The model can classify the following tomato leaf conditions:

1. Bacterial Spot  
2. Early Blight  
3. Late Blight  
4. Leaf Mold  
5. Septoria Leaf Spot  
6. Spider Mites  
7. Target Spot  
8. Tomato Yellow Leaf Curl Virus  
9. Tomato Mosaic Virus  
10. Healthy Leaf

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Gradio

---

## 📂 Project Structure

```bash
├── app.py
├── tomato_model.keras
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/tomato-leaf-disease-prediction.git
cd tomato-leaf-disease-prediction
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate environment:

#### Linux / Mac

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

After running, Gradio will generate a local URL such as:

```bash
http://127.0.0.1:7860
```

Open it in your browser.

---

## 📸 How to Use

1. Upload a tomato leaf image or use webcam input
2. Click on **Analyze Image**
3. View:
   - Predicted disease
   - Confidence score
   - Disease information
   - Recommendations

---

## 🧪 Model Workflow

1. Input image is resized to **224x224**
2. Image is normalized
3. Model predicts disease probabilities
4. Highest confidence class is selected
5. Recommendation is displayed

---

## 📊 Output Example

```text
Detected Disease: Early Blight

Confidence: 97.45%

Recommendation:
Improve air circulation and use fungicides.
```

---

## 📈 Future Improvements

- Add more plant disease datasets
- Improve model accuracy
- Deploy on cloud platforms
- Mobile application integration
- Multi-language support
- Real-time field detection

---

## ⚠️ Disclaimer

This application is designed to assist in disease detection and should not replace professional agricultural consultation.

---

## 👨‍💻 Author

Developed as a Deep Learning project for plant disease classification and smart agriculture solutions.

---

## 📜 License

This project is open-source and available for educational and research purposes.
