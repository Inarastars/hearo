from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load data from JSON file
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

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

@app.route('/api/categories')
def get_categories():
    data = load_data()
    categories = list(set(item['type'] for item in data))
    return jsonify(sorted(categories))

if __name__ == '__main__':
    app.run(debug=True)