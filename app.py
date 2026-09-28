import streamlit as st
import pickle
import pytesseract
from PIL import Image


# ============================================================
# CONFIGURATION
# ============================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# ============================================================
# LOAD MODEL
# ============================================================

with open("model/scam_detector.pkl", "rb") as file:
    model = pickle.load(file)


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="centered"
)


# ============================================================
# HEADER
# ============================================================

st.title("🛡️ ScamShield AI")

st.markdown(
    "<p style='font-size:20px; color:gray;'>"
    "AI-Powered Scam Detection & Risk Analysis"
    "</p>",
    unsafe_allow_html=True
)

st.info(
    "🔍 Analyze suspicious messages or screenshots "
    "using machine learning and OCR."
)


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown("### ⚙️ How ScamShield AI Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**1️⃣ Input**")
    st.caption("Message or screenshot")

with col2:
    st.markdown("**2️⃣ OCR**")
    st.caption("Extract text from image")

with col3:
    st.markdown("**3️⃣ ML Analysis**")
    st.caption("TF-IDF + Logistic Regression")

with col4:
    st.markdown("**4️⃣ Risk Report**")
    st.caption("Risk score + red flags")

st.divider()


# ============================================================
# MESSAGE INPUT
# ============================================================

st.markdown("### 📝 Enter a Message")

message = st.text_area(
    "Paste your suspicious message:",
    height=180,
    placeholder=(
        "Example: URGENT! Your bank account will be blocked..."
    )
)


# ============================================================
# SCREENSHOT UPLOAD
# ============================================================

st.markdown("### 📸 Or Upload a Screenshot")

uploaded_file = st.file_uploader(
    "Upload a suspicious message screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Screenshot",
        use_container_width=True
    )

    extracted_text = pytesseract.image_to_string(image)

    st.markdown("### 🔎 Extracted Text")

    if extracted_text.strip():

        st.text_area(
            "Text detected from screenshot:",
            extracted_text,
            height=150
        )

        message = extracted_text

    else:

        st.warning(
            "Could not extract readable text from this image."
        )


# ============================================================
# ANALYZE MESSAGE
# ============================================================

if st.button("🔍 Analyze Message"):

    if not message.strip():

        st.warning(
            "Please enter a message or upload a screenshot."
        )

    else:

        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        prediction = model.predict([message])[0]

        probabilities = model.predict_proba([message])[0]

        confidence = max(probabilities) * 100


        # ----------------------------------------------------
        # CONVERT DATASET LABELS
        # ----------------------------------------------------

        if prediction == "spam":

            result = "scam"

        else:

            result = "legitimate"


        # ----------------------------------------------------
        # RESULT SECTION
        # ----------------------------------------------------

        st.divider()

        st.markdown("## 📊 Analysis Result")


        # ====================================================
        # SCAM RESULT
        # ====================================================

        if result == "scam":

            st.error("🚨 Potential Scam/Spam Detected")

            st.write(
                f"**Model Confidence:** {confidence:.2f}%"
            )

            st.progress(min(int(confidence), 100))


            # ------------------------------------------------
            # RISK LEVEL
            # ------------------------------------------------

            if confidence >= 80:

                st.write("🔴 **High Risk**")

            elif confidence >= 50:

                st.write("🟠 **Medium Risk**")

            else:

                st.write("🟢 **Low Risk**")


            # ------------------------------------------------
            # RED FLAGS
            # ------------------------------------------------

            red_flags = []

            message_lower = message.lower()


            if "urgent" in message_lower:

                red_flags.append(
                    "⚠️ Uses urgent or threatening language"
                )


            if "click" in message_lower or "link" in message_lower:

                red_flags.append(
                    "🔗 Contains a request to click a link"
                )


            if "otp" in message_lower:

                red_flags.append(
                    "🔐 Mentions an OTP or authentication code"
                )


            if "bank" in message_lower:

                red_flags.append(
                    "🏦 Mentions banking or financial information"
                )


            if (
                "won" in message_lower
                or "prize" in message_lower
                or "reward" in message_lower
            ):

                red_flags.append(
                    "🎁 Contains a prize or reward claim"
                )


            if "verify" in message_lower:

                red_flags.append(
                    "🔎 Requests identity or account verification"
                )


            if (
                "password" in message_lower
                or "login" in message_lower
                or "username" in message_lower
            ):

                red_flags.append(
                    "🔑 Requests or references account credentials"
                )


            if (
                "money" in message_lower
                or "cash" in message_lower
                or "payment" in message_lower
            ):

                red_flags.append(
                    "💰 Contains financial or payment-related language"
                )


            # ------------------------------------------------
            # DISPLAY RED FLAGS
            # ------------------------------------------------

            if red_flags:

                st.markdown("### 🚩 Red Flags Detected")

                for flag in red_flags:

                    st.write(flag)

            else:

                st.markdown("### 🚩 Red Flags")

                st.write(
                    "The ML model detected spam-like patterns, "
                    "but no predefined keyword-based red flags "
                    "were triggered."
                )


        # ====================================================
        # LEGITIMATE RESULT
        # ====================================================

        else:

            st.success("✅ Message Appears Legitimate")

            st.write(
                f"**Model Confidence:** {confidence:.2f}%"
            )

            st.progress(min(int(confidence), 100))

            st.write(
                "The model classified this message as "
                "legitimate based on patterns learned from "
                "the training dataset."
            )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.markdown("### 📈 Model Performance")

st.caption(
    "Evaluation on a held-out 20% test set from the "
    "cleaned UCI SMS Spam Collection."
)


metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric(
        "Accuracy",
        "94.58%"
    )


with metric2:

    st.metric(
        "Scam Precision",
        "97%"
    )


with metric3:

    st.metric(
        "Scam Recall",
        "59%"
    )


with metric4:

    st.metric(
        "Scam F1",
        "73%"
    )


st.caption(
    "The model is trained on SMS spam/legitimate messages. "
    "Predictions indicate potential scam/spam patterns and "
    "should not be treated as definitive proof of fraud."
)


# ============================================================
# DATASET INFORMATION
# ============================================================

st.markdown("### 📚 Dataset")

st.write(
    "Training data: UCI SMS Spam Collection"
)

st.write(
    "5,572 original messages → 5,169 messages after "
    "cleaning and duplicate removal."
)


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.markdown("### 🧰 Technology Stack")

st.write(
    "Python • Pandas • Scikit-learn • TF-IDF • "
    "Logistic Regression • Tesseract OCR • Streamlit"
)