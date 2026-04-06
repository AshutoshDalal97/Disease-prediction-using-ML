from flask import Flask, render_template, request
import pickle
import json
import sqlite3
import os

app = Flask(__name__)

# Load model
model = pickle.load(open("best_model.pkl", "rb"))

with open("features.json") as f:
    features = json.load(f)

# ✅ SQLite DB connection
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptoms TEXT,
    prediction TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

@app.route('/')
def home():
    return render_template("index.html", features=features)

@app.route('/predict', methods=['POST'])
def predict():
    selected = request.form.getlist('symptoms')

    input_vector = [0] * len(features)

    for s in selected:
        if s in features:
            input_vector[features.index(s)] = 1

    probs = model.predict_proba([input_vector])[0]
    diseases = model.classes_

    results = sorted(zip(diseases, probs), key=lambda x: x[1], reverse=True)

    try:
        top_results = results[:5]

        formatted_results = ", ".join([
            f"{disease}: {round(prob*100, 2)}%" 
            for disease, prob in top_results
        ])

        # ✅ SQLite query
        query = "INSERT INTO predictions (symptoms, prediction) VALUES (?, ?)"
        cursor.execute(query, (str(selected), formatted_results))
        conn.commit()

        print("Data inserted successfully")

    except Exception as e:
        print("DB ERROR:", e)

    return render_template("result.html", results=results[:5])

# ✅ Required for deployment
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)