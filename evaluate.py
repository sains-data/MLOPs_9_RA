import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/dataset_chatbot_itera.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["intent"])

def evaluate():
    correct = 0
    total = len(df)

    for i, row in df.iterrows():
        query = row["intent"]
        q_vec = vectorizer.transform([query])
        sim = cosine_similarity(q_vec, X)
        pred_idx = sim.argmax()

        if pred_idx == i:
            correct += 1

    accuracy = correct / total
    return accuracy

if __name__ == "__main__":
    acc = evaluate()
    print(f"Accuracy: {acc:.2f}")
