let time = 0;
let interval = null;
let lapCount = 0;

const display = document.getElementById("display");
const lapsDiv = document.getElementById("laps");

function formatTime(ms) {
    let centiseconds = Math.floor((ms % 1000) / 10); // 2 digits
    let totalSeconds = Math.floor(ms / 1000);
    let seconds = totalSeconds % 60;
    let minutes = Math.floor(totalSeconds / 60) % 60;
    let hours = Math.floor(totalSeconds / 3600);

    return `${String(hours).padStart(3, '0')}:` +
           `${String(minutes).padStart(2, '0')}:` +
           `${String(seconds).padStart(2, '0')}.` +
           `${String(centiseconds).padStart(2, '0')}`;
}
function updateDisplay() {
    display.textContent = formatTime(time);
}
document.getElementById("start").onclick = () => {
    if (interval) return;

    interval = setInterval(() => {
        time += 10;
        updateDisplay();
    }, 10);
};
document.getElementById("stop").onclick = () => {
    clearInterval(interval);
    interval = null;
};
document.getElementById("reset").onclick = () => {
    clearInterval(interval);
    interval = null;
    time = 0;
    lapCount = 0;
    updateDisplay();
    lapsDiv.innerHTML = "";
};
document.getElementById("add").onclick = () => {
    time += 5000;
    updateDisplay();
};
document.getElementById("sub").onclick = () => {
    time = Math.max(0, time - 5000);
    updateDisplay();
};
document.getElementById("lap").onclick = () => {
    if (!interval) return;

    const lap = document.createElement("div");
    lap.textContent = `Lap ${lapCount}: ${formatTime(time)}`;
    lapCount++;
    lapsDiv.prepend(lap);
};
