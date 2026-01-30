from flask import Flask, render_template, request
from recommender import recommend

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def get_recommendations():
    movie = request.form["movie"]
    recs = recommend(movie)
    return render_template("index.html", movies=recs, name=movie)

if __name__ == "__main__":
    app.run(debug=True)
