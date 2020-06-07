const interval = 1000;
const time = 30;
const initialOffset = 440;
const slice = initialOffset / time;

const timeLeft = document.getElementById("time-left");
const circle = document.getElementById('circle');

function getColor(timeLeft) {
    if (timeLeft > 10 || timeLeft === 1) return "#6fdb6f";
    else if (timeLeft > 5) return "orange";
    else return "red";
}

function formatTime(time) {
    const minutes = Math.floor(time / 60);
    let seconds = time % 60;

    if (seconds < 10) {
      seconds = `0${seconds}`;
    }
  
    return `${minutes}:${seconds}`;
  }
  
function updateTokens() {
  fetch('/tokens')
    .then(response => response.json())
    .then(data => {
        timeLeft.innerHTML = formatTime(data.timeLeft);
        circle.style.strokeDashoffset = initialOffset - ((data.timeLeft-1) * slice);
        circle.style.stroke = getColor(data.timeLeft);
        circle.style.fill = "rgba(50,50,50,0.15)";
        
        data.tokens.forEach((token, index) => {
            const elem = document.getElementById("anchor-" + index);
            elem.innerHTML = token;
        });
    });
}

function init() {
  new ClipboardJS(".token");
  setInterval(updateTokens, interval);
}
