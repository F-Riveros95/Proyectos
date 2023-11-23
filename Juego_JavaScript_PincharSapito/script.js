const frog = document.querySelector('.frog');
const scoreElement = document.getElementById('score');
const timerElement = document.getElementById('timer');
const frogSound = document.getElementById('frogSound');

let score = 0;
let timeLeft = 30;

frog.addEventListener('click', () => {
  increaseScore();
  playFrogSound();
  moveFrogRandomly();
});

function increaseScore() {
  score++;
  scoreElement.textContent = score;
}

function playFrogSound() {
  frogSound.currentTime = 0;
  frogSound.play();
}

function moveFrogRandomly() {
    const maxX = window.innerWidth * 0.7 - frog.offsetWidth;
    const maxY = window.innerHeight * 0.7 - frog.offsetHeight;
    const randomX = Math.floor(Math.random() * maxX);
    const randomY = Math.floor(Math.random() * maxY);
    
    frog.style.left = randomX + 'px';
    frog.style.top = randomY + 'px';
  }

function updateTimer() {
  timerElement.textContent = timeLeft ;
}

function countdown() {
  updateTimer();
  const countdownInterval = setInterval(() => {
    timeLeft--;
    updateTimer();

    if (timeLeft <= 0) {
      clearInterval(countdownInterval);
      frog.removeEventListener('click', handleGameClick);
      alert('Genial! Pudiste pincharlo: ' + score + ' veces');
    }
  }, 1000);
}

function handleGameClick() {
  increaseScore();
  playFrogSound();
  moveFrogRandomly();
}

frog.addEventListener('click', () => {
    moveFrogRandomly();
  });

countdown();
