import pandas as pd
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PATH DATASET ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "dataset_chatbot_itera.csv")

df = pd.read_csv(DATA_PATH)

# ---------------- TEXT NORMALIZATION ----------------
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

# ---------------- MODEL (TF-IDF) ----------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["question_keywords"])

# ---------------- INFERENCE ----------------
def get_answer(user_input):
    user_input = normalize(user_input)
    user_vec = vectorizer.transform([user_input])
    sim = cosine_similarity(user_vec, X)
    idx = sim.argmax()

    if sim[0][idx] < 0.2:
        return "Maaf, saya belum memahami pertanyaan Anda."

    return df.iloc[idx]["answer"]
