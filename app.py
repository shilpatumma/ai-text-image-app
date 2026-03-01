# import pickle
# import os
# from PIL import Image

# # Load model
# model = pickle.load(open("model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # Take input
# user_input = input("Enter object name: ")

# # Predict
# input_vector = vectorizer.transform([user_input])
# prediction = model.predict(input_vector)[0]

# print("Predicted:", prediction)

# # Show image
# image_path = f"images/{prediction}.jpg"

# if os.path.exists(image_path):
#     img = Image.open(image_path)
#     img.show()
# else:
#     print("Image not found!")





from flask import Flask, render_template, request
import joblib
import os
import pandas as pd

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load labels from dataset
data = pd.read_csv("data.csv")
labels = sorted(data["label"].unique())

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None
    image_file = None

    if request.method == "POST":
        user_input = request.form.get("text")

        if user_input:
            text_vector = vectorizer.transform([user_input])
            prediction = model.predict(text_vector)[0]
            confidence = model.predict_proba(text_vector).max() * 100

            image_path = f"static/{prediction}.jpg"

            if os.path.exists(image_path):
                image_file = f"{prediction}.jpg"

    return render_template("index.html",
                           prediction=prediction,
                           confidence=confidence,
                           image_file=image_file,
                           labels=labels)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)