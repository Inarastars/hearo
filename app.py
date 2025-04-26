from flask import Flask, render_template, jsonify, request
import json
import os
import joblib
import numpy as np

app = Flask(__name__)

# Load data from JSON file
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

# Load the model and label encoder
model = joblib.load("models/xgb_hand_gesture_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/translate')
def translate():
    return render_template('translate.html')

@app.route('/api/data')
def get_data():
    data = load_data()
    return jsonify(data)

@app.route('/api/data/category/<category>')
def get_data_by_category(category):
    data = load_data()
    filtered_data = [item for item in data if item['type'] == category]
    return jsonify(filtered_data)

@app.route('/api/categories')
def get_categories():
    data = load_data()
    categories = list(set(item['type'] for item in data))
    return jsonify(categories)

@app.route('/api/predict', methods=['POST'])
def predict_sign():
    data = request.json.get('landmarks', [])
    if not data:
        return jsonify({'error': 'No landmarks provided'}), 400

    try:
        # Prepare data for prediction
        flattened_data = []
        for landmark in data:
            flattened_data.extend([landmark['x'], landmark['y'], landmark['z']])
        
        prediction = model.predict([flattened_data])[0]
        label = label_encoder.inverse_transform([prediction])[0]

        return jsonify({'label': label})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)