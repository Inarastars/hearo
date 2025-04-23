// script.js
document.addEventListener('DOMContentLoaded', function()
{
    let
currentQuestion = 1;
const
totalQuestions = 10;
let
score = 0;
let
answers = {};
let
isAnswered = false;

const
questionContainers = document.querySelectorAll('.question-container');
const
nextBtn = document.querySelector('.next-btn');
const
prevBtn = document.querySelector('.prev-btn');
const
checkBtn = document.querySelector('.check-btn');
const
resultContainer = document.querySelector('.result-container');
const
progressBar = document.querySelector('#progress');
const
questionNumber = document.querySelector('#question-number');
const
scoreElement = document.querySelector('#score');
const
detailedResults = document.querySelector('#detailed-results');
const
restartBtn = document.querySelector('.restart-btn');

// Инициализация
квиза
updateProgressBar();

// Обработка
выбора
варианта
ответа
questionContainers.forEach(container= > {
    const
options = container.querySelectorAll('.option');
options.forEach(option= > {
    option.addEventListener('click', function()
{
if (isAnswered)
return; // Если
ответ
уже
проверен, ничего
не
делаем

// Снимаем
выделение
с
других
вариантов
options.forEach(opt= > opt.classList.remove('selected'));

// Выделяем
выбранный
вариант
this.classList.add('selected');

// Активируем
кнопку
проверки
checkBtn.disabled = false;
});
});
});

// Кнопка
"Проверить"
checkBtn.addEventListener('click', function()
{
    const
currentContainer = document.querySelector(`.question - container[data - question = "${currentQuestion}"]`);
const
selectedOption = currentContainer.querySelector('.option.selected');

if (!selectedOption)
{
    alert('Пожалуйста, выберите вариант ответа');
return;
}

// Отмечаем
правильный
и
неправильный
ответы
const
options = currentContainer.querySelectorAll('.option');
options.forEach(option= > {
if (option.hasAttribute('data-correct'))
{
    option.classList.add('correct');
}
});

// Если
выбран
неправильный
вариант, отмечаем
его
красным
if (!selectedOption.hasAttribute('data-correct')) {
selectedOption.classList.add('incorrect');
}

// Сохраняем
ответ
answers[currentQuestion] = {
selected: selectedOption,
isCorrect: selectedOption.hasAttribute('data-correct')
};

// Деактивируем
кнопку
проверки
и
активируем
кнопку
"Далее"
checkBtn.disabled = true;
nextBtn.disabled = false;
isAnswered = true;
});

// Кнопка
"Далее"
nextBtn.addEventListener('click', function()
{
// Если
это
последний
вопрос
и
на
него
ответили
if (currentQuestion === totalQuestions & & isAnswered)
{
showResults();
return;
}

// Переходим
к
следующему
вопросу
currentQuestion + +;
isAnswered = false; // Сбрасываем
флаг
ответа
updateQuestionDisplay();
updateProgressBar();
});

// Кнопка
"Назад"
prevBtn.addEventListener('click', function()
{
if (currentQuestion > 1)
{
currentQuestion - -;
isAnswered = answers[currentQuestion] ? true: false;
updateQuestionDisplay();
updateProgressBar();
}
});

// Кнопка
"Начать заново"
restartBtn.addEventListener('click', function()
{
    resetQuiz();
});

// Функция
обновления
отображения
вопроса
function
updateQuestionDisplay()
{
    questionContainers.forEach(container= > {
container.classList.remove('active');
});

const
currentContainer = document.querySelector(`.question - container[data - question = "${currentQuestion}"]`);
currentContainer.classList.add('active');

// Обновляем
состояние
кнопок
prevBtn.disabled = currentQuestion == = 1;

// Если
на
этот
вопрос
уже
отвечали
if (answers[currentQuestion])
{
    nextBtn.disabled = false;
checkBtn.disabled = true;

// Восстанавливаем
стили
ответов
const
options = currentContainer.querySelectorAll('.option');
options.forEach(option= > {
if (option === answers[currentQuestion].selected)
{
    option.classList.add('selected');
if (!option.hasAttribute('data-correct')) {
    option.classList.add('incorrect');
}
}

if (option.hasAttribute('data-correct')) {
option.classList.add('correct');
}
});

isAnswered = true;
} else {
nextBtn.disabled = true;
checkBtn.disabled = false;

// Сбрасываем стили для новых вопросов
const options = currentContainer.querySelectorAll('.option');
options.forEach(option = > {
option.classList.remove('selected', 'correct', 'incorrect');
});

isAnswered = false;
}

// Обновляем номер вопроса
questionNumber.textContent = `Вопрос ${currentQuestion} из ${totalQuestions}`;

// Если на текущем вопросе уже выбран ответ но не проверен
const selected = currentContainer.querySelector('.option.selected');
if (selected & & !isAnswered) {
checkBtn.disabled = false;
} else if (!selected & & !isAnswered) {
checkBtn.disabled = false;
}

// Меняем текст кнопки Далее на последнем вопросе
nextBtn.textContent = currentQuestion == = totalQuestions ? 'Завершить': 'Далее';
}

// Функция
обновления
прогресс - бара
function
updateProgressBar()
{
    const
progress = (currentQuestion / totalQuestions) * 100;
progressBar.style.width = `${progress} % `;
}

// Функция
отображения
результатов
function
showResults()
{
    questionContainers.forEach(container= > {
container.classList.remove('active');
});

// Подсчет
правильных
ответов
score = 0;
let
detailedResultsHTML = '';

for (let i = 1; i <= totalQuestions; i++)
{
    const
isCorrect = answers[i] & & answers[i].isCorrect;
if (isCorrect)
{
score + +;
}

// Генерируем
подробные
результаты
const
questionText = document.querySelector(`.question - container[data - question = "${i}"].question
`).textContent;
const
resultClass = isCorrect ? 'correct': 'incorrect';
const
resultStatus = isCorrect ? 'Верно': 'Неверно';

detailedResultsHTML += `
                       < div


class ="result-item ${resultClass}" >

< p > < strong > Вопрос ${i}: < / strong > ${questionText} < / p >
< p > < strong > Результат: < / strong > ${resultStatus} < / p >
< / div >
`;
}

scoreElement.textContent = score;
detailedResults.innerHTML = detailedResultsHTML;
resultContainer.style.display = 'block';

// Скрываем
кнопки
навигации
nextBtn.style.display = 'none';
prevBtn.style.display = 'none';
checkBtn.style.display = 'none';
}

// Функция
сброса
квиза
function
resetQuiz()
{
// Сбрасываем
все
ответы
answers = {};
score = 0;
currentQuestion = 1;
isAnswered = false;

// Убираем
выбранные
варианты
document.querySelectorAll('.option').forEach(option= > {
    option.classList.remove('selected', 'correct', 'incorrect');
});

// Скрываем
результаты
resultContainer.style.display = 'none';

// Показываем
первый
вопрос
updateQuestionDisplay();
updateProgressBar();

// Возвращаем
кнопки
навигации
nextBtn.style.display = 'block';
prevBtn.style.display = 'block';
checkBtn.style.display = 'block';

// Сбрасываем
состояние
кнопок
nextBtn.disabled = true;
prevBtn.disabled = true;
checkBtn.disabled = false;
}
});