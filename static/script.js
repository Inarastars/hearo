document.addEventListener('DOMContentLoaded', function() {
    // Navigation
    const navButtons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section');

    navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const sectionId = btn.dataset.section;
            
            // Update navigation
            navButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Update sections
            sections.forEach(section => {
                section.classList.add('hidden');
                if (section.id === sectionId) {
                    section.classList.remove('hidden');
                }
            });
        });
    });

    // Flashcards
    async function loadFlashcards() {
        try {
            const response = await fetch('/api/flashcards');
            const flashcards = await response.json();
            const container = document.getElementById('flashcards-container');
            
            flashcards.forEach(card => {
                const cardElement = document.createElement('div');
                cardElement.className = 'flashcard';
                cardElement.innerHTML = `
                    <h3 class="text-xl font-bold mb-2">${card.word}</h3>
                    <video src="${card.video_url}" class="w-full rounded" loop></video>
                `;
                container.appendChild(cardElement);
            });
        } catch (error) {
            console.error('Error loading flashcards:', error);
        }
    }

    // Live Translator
    async function setupTranslator() {
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        const hands = new Hands({locateFile: (file) => {
            return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
        }});

        hands.setOptions({
            maxNumHands: 2,
            modelComplexity: 1,
            minDetectionConfidence: 0.5,
            minTrackingConfidence: 0.5
        });

        // Add hands tracking logic here
    }

    loadFlashcards();
    setupTranslator();
});
