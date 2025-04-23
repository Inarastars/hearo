/* styles.css */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
}

.quiz-container {
    background-color: white;
    border-radius: 10px;
    padding: 25px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 30px;
}

.question-container {
    margin-bottom: 40px;
    display: none;
}

.question-container.active {
    display: block;
}

.question {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #2c3e50;
}

.options-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 15px;
}

.option {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    border: 2px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    transition: all 0.3s ease;
}

.option:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.option img {
    width: 180px;
    height: 180px;
    object-fit: cover;
    border-radius: 5px;
    margin-bottom: 10px;
}

.option-label {
    text-align: center;
    font-weight: bold;
}

.option.selected {
    border-color: #3498db;
    background-color: #f0f8ff;
}

.option.correct {
    border-color: #2ecc71;
    background-color: #d4f7e2;
}

.option.incorrect {
    border-color: #e74c3c;
    background-color: #fadbd8;
}

.control-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.btn {
    padding: 12px 25px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s;
}

.next-btn, .check-btn {
    background-color: #3498db;
    color: white;
}

.next-btn:hover, .check-btn:hover {
    background-color: #2980b9;
}

.prev-btn {
    background-color: #bdc3c7;
    color: #2c3e50;
}

.prev-btn:hover {
    background-color: #a6acaf;
}

.next-btn:disabled, .prev-btn:disabled, .check-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.progress-container {
    margin-bottom: 20px;
}

.progress-bar {
    height: 10px;
    background-color: #ecf0f1;
    border-radius: 5px;
    overflow: hidden;
}

.progress {
    height: 100%;
    background-color: #3498db;
    width: 10%;
}

.result-container {
    text-align: center;
    display: none;
}

.result-container h2 {
    margin-bottom: 20px;
    color: #2c3e50;
}

.score {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.restart-btn {
    background-color: #2ecc71;
    color: white;
    padding: 12px 25px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
}

.restart-btn:hover {
    background-color: #27ae60;
}

.detailed-results {
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: left;
    padding: 15px;
    background-color: #f9f9f9;
    border-radius: 8px;
    max-height: 300px;
    overflow-y: auto;
}

.result-item {
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 5px;
}

.result-item.correct {
    background-color: #d4f7e2;
}

.result-item.incorrect {
    background-color: #fadbd8;
}