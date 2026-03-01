# # import pickle
# # import os
# # import tkinter as tk
# # from PIL import Image, ImageTk

# # # Load model
# # model = pickle.load(open("model.pkl", "rb"))
# # vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # def predict():
# #     user_input = entry.get()
# #     input_vector = vectorizer.transform([user_input])
# #     prediction = model.predict(input_vector)[0]

# #     image_path = f"images/{prediction}.jpg"

# #     if os.path.exists(image_path):
# #         img = Image.open(image_path)
# #         img = img.resize((200, 200))
# #         img = ImageTk.PhotoImage(img)
# #         panel.config(image=img)
# #         panel.image = img
# #     else:
# #         result_label.config(text="Image not found!")

# # # GUI window
# # root = tk.Tk()
# # root.title("Text to Image ML App")

# # entry = tk.Entry(root)
# # entry.pack(pady=10)

# # btn = tk.Button(root, text="Predict", command=predict)
# # btn.pack()

# # panel = tk.Label(root)
# # panel.pack()

# # result_label = tk.Label(root, text="")
# # result_label.pack()

# # root.mainloop()








# # def predict():
# #     user_input = entry.get()
    
# #     # Clear previous text
# #     result_label.config(text="")
    
# #     # Predict
# #     input_vector = vectorizer.transform([user_input])
# #     prediction = model.predict(input_vector)[0]

# #     image_path = f"images/{prediction}.jpg"

# #     # Clear previous image first
# #     panel.config(image="")
# #     panel.image = None

# #     if os.path.exists(image_path):
# #         img = Image.open(image_path)
# #         img = img.resize((200, 200))
# #         img = ImageTk.PhotoImage(img)
# #         panel.config(image=img)
# #         panel.image = img
# #     else:
# #         result_label.config(text="Image not found!")






# import pickle
# import os
# import tkinter as tk
# from PIL import Image, ImageTk

# # Load model
# model = pickle.load(open("model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # def predict():
# #     user_input = entry.get()
    
# #     # Clear previous text
# #     result_label.config(text="")
    
# #     # Predict
# #     input_vector = vectorizer.transform([user_input])
# #     prediction = model.predict(input_vector)[0]

# #     image_path = f"images/{prediction}.jpg"

# #     # Clear previous image
# #     panel.config(image="")
# #     panel.image = None

# #     if os.path.exists(image_path):
# #         img = Image.open(image_path)
# #         img = img.resize((200, 200))
# #         img = ImageTk.PhotoImage(img)
# #         panel.config(image=img)
# #         panel.image = img
# #     else:
# #         result_label.config(text="Image not found!")

# def predict():
#     user_input = entry.get().lower()
    
#     result_label.config(text="")
#     panel.config(image="")
#     panel.image = None

#     input_vector = vectorizer.transform([user_input])
    
#     prediction = model.predict(input_vector)[0]
#     probabilities = model.predict_proba(input_vector)

#     confidence = max(probabilities[0]) * 100

#     image_path = f"images/{prediction}.jpg"

#     if os.path.exists(image_path):
#         img = Image.open(image_path)
#         img = img.resize((200, 200))
#         img = ImageTk.PhotoImage(img)
#         panel.config(image=img)
#         panel.image = img
        
#         result_label.config(
#             text=f"Prediction: {prediction}\nConfidence: {confidence:.2f}%"
#         )
#     else:
#         result_label.config(text="Image not found!")


# # GUI window
# root = tk.Tk()
# root.title("Text to Image ML App")
# root.geometry("300x350")

# entry = tk.Entry(root)
# entry.pack(pady=10)

# btn = tk.Button(root, text="Predict", command=predict)
# btn.pack()

# panel = tk.Label(root)
# panel.pack(pady=10)

# result_label = tk.Label(root, text="")
# result_label.pack()

# root.mainloop()








# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import joblib
# import os

# # Load model and vectorizer
# model = joblib.load("model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")

# # Create main window
# root = tk.Tk()
# root.title("Text to Image ML App")
# root.geometry("400x500")

# # Dropdown options (your labels)
# options = ["cat", "pen", "car"]

# # Create dropdown
# selected_value = tk.StringVar()
# dropdown = ttk.Combobox(root, textvariable=selected_value, values=options, state="readonly")
# dropdown.pack(pady=10)

# # Label for showing image
# image_label = tk.Label(root)
# image_label.pack(pady=20)

# # Label for confidence
# result_label = tk.Label(root, text="")
# result_label.pack()

# def show_image(event=None):
#     text = selected_value.get()

#     # Convert text to vector
#     text_vector = vectorizer.transform([text])

#     # Predict
#     prediction = model.predict(text_vector)[0]
#     probability = model.predict_proba(text_vector).max() * 100

#     image_path = f"images/{prediction}.jpg"

#     if os.path.exists(image_path):
#         img = Image.open(image_path)
#         img = img.resize((250, 250))
#         img = ImageTk.PhotoImage(img)

#         image_label.config(image=img)
#         image_label.image = img
#         result_label.config(text=f"Prediction: {prediction}\nConfidence: {probability:.2f}%")
#     else:
#         image_label.config(image="")
#         result_label.config(text="Image not found!")

# # When dropdown changes
# dropdown.bind("<<ComboboxSelected>>", show_image)

# root.mainloop()





import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import joblib
import os
import pandas as pd

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load dataset to auto-get labels
data = pd.read_csv("data.csv")
labels = sorted(data["label"].unique())

# Create main window
root = tk.Tk()
root.title("🔥 Smart Text to Image App")
root.geometry("500x600")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(root, text="AI Text to Image Viewer",
                 font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Frame
frame = tk.Frame(root, bg="#2b2b40", padx=20, pady=20)
frame.pack(pady=20)

# Text Entry
entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Dropdown (Auto from CSV)
selected_value = tk.StringVar()
dropdown = ttk.Combobox(frame,
                        textvariable=selected_value,
                        values=labels,
                        state="readonly")
dropdown.pack(pady=10)

# Image Label
image_label = tk.Label(root, bg="#1e1e2f")
image_label.pack(pady=20)

# Result Label
result_label = tk.Label(root,
                        text="",
                        font=("Arial", 12),
                        bg="#1e1e2f",
                        fg="white")
result_label.pack()

# Confidence Bar
progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(pady=10)

def predict_and_show(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    probability = model.predict_proba(text_vector).max() * 100

    image_path = f"images/{prediction}.jpg"

    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)

        image_label.config(image=img)
        image_label.image = img

        result_label.config(
            text=f"Prediction: {prediction}\nConfidence: {probability:.2f}%"
        )

        progress["value"] = probability
    else:
        image_label.config(image="")
        result_label.config(text="Image not found!")
        progress["value"] = 0

def dropdown_selected(event=None):
    text = selected_value.get()
    entry.delete(0, tk.END)
    entry.insert(0, text)
    predict_and_show(text)

def button_click():
    text = entry.get()
    if text:
        predict_and_show(text)

# Predict Button
predict_btn = tk.Button(frame,
                        text="Predict",
                        command=button_click,
                        bg="#4CAF50",
                        fg="white",
                        font=("Arial", 12),
                        padx=10,
                        pady=5)
predict_btn.pack(pady=10)

dropdown.bind("<<ComboboxSelected>>", dropdown_selected)

root.mainloop()






