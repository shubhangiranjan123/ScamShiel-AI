# 🛡️ ScamShield AI

### AI-Powered Scam Detection & Risk Analysis System

ScamShield AI is a machine-learning based system that analyzes suspicious SMS messages and screenshots to identify potential scam/spam patterns.

The system combines **Natural Language Processing (NLP), machine learning, OCR, and rule-based red-flag analysis** to generate an interpretable risk report.

---

## 🚀 Features

- 📝 Analyze suspicious text messages
- 📸 Upload screenshots of messages
- 🔎 Extract text from screenshots using Tesseract OCR
- 🤖 Machine-learning based spam/scam classification
- 📊 Model confidence score
- 🚩 Explainable red-flag detection
- 🛡️ Risk-level assessment
- 🌐 Interactive Streamlit web interface

---

## 🧠 Machine Learning Pipeline

```text
Message / Screenshot
        ↓
   Text Extraction
        ↓
   Text Preprocessing
        ↓
      TF-IDF
        ↓
Logistic Regression
        ↓
 Scam / Legitimate
        ↓
Confidence + Red Flags
        ↓
    Risk Report
    📊 Dataset

The model is trained using the UCI SMS Spam Collection dataset.

Dataset characteristics:

Original messages: 5,572
Messages after cleaning and duplicate removal: 5,169
Legitimate messages: 4,516
Spam messages: 653

The dataset contains real SMS messages labeled as either legitimate (ham) or spam (spam).

Dataset Source

UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection

The dataset is distributed under the CC BY 4.0 license.

🤖 Machine Learning Model

The project uses a Scikit-learn pipeline consisting of:

TF-IDF Vectorization

TF-IDF converts text into numerical features based on the importance of words and phrases within the dataset.

The model uses:

Lowercase conversion
English stop-word removal
Unigrams and bigrams
Logistic Regression

Logistic Regression is used as the classification algorithm.

Class balancing is enabled using:

class_weight="balanced"

This helps address the imbalance between legitimate and spam messages.

📈 Model Performance

Evaluation was performed on a held-out 20% test set containing 1,034 messages.

Metric	Result
Accuracy	97.49%
Spam Precision	91%
Spam Recall	89%
Spam F1 Score	90%
Confusion Matrix
[[892   11]
 [ 15  116]]

The model correctly identified 116 out of 131 spam messages in the test set.

📸 OCR Processing

ScamShield AI can analyze screenshots of suspicious messages.

The OCR pipeline uses Tesseract OCR to extract text from uploaded images before sending the extracted text to the machine-learning model.

Screenshot
    ↓
Tesseract OCR
    ↓
Extracted Text
    ↓
ML Classification
🧰 Technology Stack
Python
Pandas
Scikit-learn
TF-IDF
Logistic Regression
Tesseract OCR
Pytesseract
Pillow
Streamlit
📁 Project Structure
ScamShiel-AI/
│
├── data/
│   └── SMSSpamCollection
│
├── model/
│   └── scam_detector.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ScamShiel-AI
2. Create a virtual environment
python -m venv venv
3. Activate the environment

Windows:

venv\Scripts\activate
4. Install Python dependencies
pip install -r requirements.txt
5. Install Tesseract OCR

ScamShield AI requires the Tesseract OCR engine for screenshot analysis.

After installing Tesseract, update the executable path in app.py if necessary.

▶️ Running the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🔄 Retraining the Model

To retrain the model using the dataset:

python train_model.py

The trained model is saved as:

model/scam_detector.pkl
⚠️ Limitations
The model is trained on the UCI SMS Spam Collection, which focuses on SMS spam rather than every possible modern scam category.
OCR accuracy depends on screenshot quality.
A machine-learning prediction is not proof that a message is fraudulent.
The system should be treated as a decision-support tool rather than a replacement for human verification.
🔮 Future Improvements
Transformer-based NLP models
URL and domain reputation analysis
Multilingual scam detection
Phone-number and sender analysis
Advanced explainable AI techniques
Real-time threat intelligence integration
Improved multimodal analysis for images and text
👩‍💻 Author

Shubhangi

B.E. Computer Science & Engineering (AI/ML)

📄 License

This project is intended for educational and portfolio purposes.

The SMS dataset used by this project is provided by the UCI Machine Learning Repository and is subject to its respective licensing terms.

