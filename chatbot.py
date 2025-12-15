import pandas as pd
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PATH DATASET ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "dataset_chatbot_itera.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Gabungkan keyword dan intent untuk model supaya lebih robust
df["text_for_model"] = df["question_keywords"] + " " + df["intent"]

# ---------------- TEXT NORMALIZATION ----------------
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # hapus simbol
    text = re.sub(r"\d+", "", text)      # hapus angka
    # contoh beberapa kata anak-anak / typo umum
    text = text.replace("bukain", "buka")
    text = text.replace("pinjem", "pinjam")
    text = text.replace("ta", "tugas akhir")
    return text

# ---------------- MODEL (TF-IDF) ----------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text_for_model"])

# ---------------- INFERENCE ----------------
def get_answer(user_input):
    user_input = normalize(user_input)
    user_vec = vectorizer.transform([user_input])
    sim = cosine_similarity(user_vec, X)
    idx = sim.argmax()

    # Threshold lebih fleksibel untuk pertanyaan anak
    if sim[0][idx] < 0.15:
        return "Coba tanya dengan kata lain, saya bisa jawab pertanyaan tentang perpustakaan."

    return df.iloc[idx]["answer"]

# ---------------- TEST ----------------
if __name__ == "__main__":
    print("Chatbot Perpustakaan ITERA (HIKDS)")
    print("Ketik 'keluar' untuk berhenti.\n")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ["keluar", "exit", "quit"]:
            print("Chatbot: Sampai jumpa!")
            break
        answer = get_answer(user_input)
        print("Chatbot:", answer)
