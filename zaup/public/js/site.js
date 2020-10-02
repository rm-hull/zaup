const interval = 1000;
const time = 30;
const initialOffset = 440;
const slice = initialOffset / time;

const timeLeft = document.getElementById("time-left");
const circle = document.getElementById('circle');

var handle = null;
var timerId = null;

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

function glow(elem, duration) {
  elem.classList.add("glow");
  setTimeout(() => elem.classList.remove("glow"), duration || 500);
}

function updateTokens() {
  fetch('/tokens')
    .then(response => response.json())
    .then(data => {
      timeLeft.innerHTML = formatTime(data.timeLeft);
      circle.style.strokeDashoffset = initialOffset - ((data.timeLeft - 1) * slice);
      circle.style.stroke = getColor(data.timeLeft);
      circle.style.fill = "rgba(50,50,50,0.15)";

      data.tokens.forEach((token, index) => {
        const elem = document.getElementById("anchor-" + index);
        if (data.timeLeft === 30) {
          glow(elem);
        }
        elem.innerHTML = token;
      })

    })
    .catch(err => {
      if (handle) {
        clearInterval(handle);
        document.getElementById("modal").classList.add("show");
        handle = null;
      }
      console.error(err);
    });
}

function showSnackbarMessage(message, duration = 5000) {
  const snackbar = document.getElementById('snackbar');
  document.getElementById("snackbar-message").innerText = message;
  snackbar.classList.add("show");
  if (timerId) {
    clearTimeout(timerId);
  }
  timerId = setTimeout(() => snackbar.classList.remove("show"), duration);
}

function init() {
  const clipboard = new ClipboardJS(".token");
  clipboard.on('success', e => showSnackbarMessage(`Copied "${e.text}" to the clipboard.`));
  updateTokens();
  handle = setInterval(updateTokens, interval);

  // Stop annoying flicker of green snackbar message on startup
  const snackbar = document.getElementById('snackbar');
  snackbar.classList.remove("hide");
}