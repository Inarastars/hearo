# Hearo - International Sign Language Learning App

Hearo is an interactive web application designed to help users learn International Sign Language (ISL) through flashcards, quizzes, and real-time hand gesture recognition.

## Features

- Interactive ISL flashcards
- Quiz system with progress tracking
- Live hand gesture recognition
- Popular phrases with 3D animations
- Social sharing functionality

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

### Development
```bash
python app.py
```
The app will be available at `http://localhost:5000`

### Production
```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

## Technology Stack

- Flask (Python web framework)
- TailwindCSS (Styling)
- MediaPipe (Hand tracking)
- Model Viewer (3D animations)

## License

[MIT License](license)
