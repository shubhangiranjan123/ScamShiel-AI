import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import pickle


# ---------------------------------------------
# 1. LOAD REAL DATASET
# ---------------------------------------------

data = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "text"]
)

print("Dataset loaded successfully!")
print("Total messages:", len(data))


# ---------------------------------------------
# 2. CLEAN DATA
# ---------------------------------------------

data = data.dropna()
data = data.drop_duplicates()

print("Messages after cleaning:", len(data))


# ---------------------------------------------
# 3. CLASS DISTRIBUTION
# ---------------------------------------------

print("\nClass distribution:")
print(data["label"].value_counts())


# ---------------------------------------------
# 4. SEPARATE FEATURES AND LABELS
# ---------------------------------------------

X = data["text"]
y = data["label"]


# ---------------------------------------------
# 5. SPLIT DATA
# ---------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------------------
# 6. CREATE ML PIPELINE
# ---------------------------------------------

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )
    )
])


# ---------------------------------------------
# 7. TRAIN MODEL
# ---------------------------------------------

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model trained successfully!")


# ---------------------------------------------
# 8. MAKE PREDICTIONS
# ---------------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------------
# 9. EVALUATE MODEL
# ---------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["legitimate", "scam"]
    )
)

print("Confusion Matrix:")

print(confusion_matrix(y_test, y_pred))


# ---------------------------------------------
# 10. SAVE MODEL
# ---------------------------------------------

with open("scam_detector.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as scam_detector.pkl")