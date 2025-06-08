from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.joblib")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area']
    input_data = [float(request.form[f]) for f in features]
    prediction = model.predict([input_data])[0]
    label = "Malignant" if prediction == 1 else "Benign"
    return render_template("index.html", prediction_text=f"Tumor is likely: {label}")

if __name__ == '__main__':
    app.run(debug=True)
