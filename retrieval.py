from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path(__file__).resolve().parents[2] / "data" / "knowledge.txt"

def load_documents():
    text = DATA.read_text(encoding="utf-8")
    return [x.strip() for x in text.split("\n\n") if x.strip()]

def retrieve(query: str, k: int = 3):
    docs = load_documents()
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).ravel()
    order = scores.argsort()[::-1][:k]
    return [{"text": docs[i], "score": float(scores[i])} for i in order if scores[i] > 0]
