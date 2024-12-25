let isCalculatingTheory = true; // Flag para alternar entre calcular teoria e aplicação
let theoryOscillation = 0;
let practiceOscillation = 0;

// Elementos HTML
const pointTheory = document.getElementById('point-theory');
const pointPractice = document.getElementById('point-practice');
const line = document.getElementById('line');
const uncertaintyText = document.getElementById('uncertainty');
const btn = document.getElementById('verificacao-btn');

// Função para gerar oscilação
function oscillate() {
    if (isCalculatingTheory) {
        theoryOscillation = Math.sin(Date.now() / 1000) * 10; // Oscilação no eixo Y
        pointTheory.style.top = `calc(50% + ${theoryOscillation}%)`;
        uncertaintyText.textContent = 'Oscilando a teoria';
    } else {
        practiceOscillation = Math.sin(Date.now() / 1000) * 10; // Oscilação no eixo X
        pointPractice.style.left = `calc(80% + ${practiceOscillation}%)`;
        uncertaintyText.textContent = 'Oscilando a aplicação';
    }
    line.style.width = `${Math.abs(80 - parseFloat(pointPractice.style.left))}%`;
}

// Alternar entre teoria e aplicação
btn.addEventListener('click', () => {
    isCalculatingTheory = !isCalculatingTheory;
    if (isCalculatingTheory) {
        uncertaintyText.textContent = 'Incerteza crescente';
    }
});

// Iniciar oscilação
setInterval(oscillate, 100);

