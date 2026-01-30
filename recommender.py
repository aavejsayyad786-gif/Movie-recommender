import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("movies.csv")

# Combine genre + description
data["content"] = data["genre"] + " " + data["description"]

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(data["content"])

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie = movie.lower()

    if movie not in data["title"].str.lower().values:
        return ["Movie not found in database"]

    idx = data[data["title"].str.lower()==movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x:x[1], reverse=True)

    recommendations = []
    for i in scores[1:6]:
        recommendations.append(data.iloc[i[0]].title)

    return recommendations
