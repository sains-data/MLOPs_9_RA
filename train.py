import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/dataset_chatbot_itera.csv")

with mlflow.start_run():
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["intent"])

    # evaluasi sederhana
    correct = 0
    for i, row in df.iterrows():
        q_vec = vectorizer.transform([row["intent"]])
        sim = cosine_similarity(q_vec, X)
        if sim.argmax() == i:
            correct += 1

    accuracy = correct / len(df)

    mlflow.log_param("model_type", "TF-IDF + Cosine Similarity")
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(vectorizer, "vectorizer")

