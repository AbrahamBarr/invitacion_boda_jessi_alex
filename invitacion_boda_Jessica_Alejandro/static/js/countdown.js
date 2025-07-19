const targetDate = new Date("2025-11-15T18:00:00").getTime();
function updateCountdown() {
  const now = new Date().getTime();
  const distance = targetDate - now;
  if (distance < 0) {
    document.getElementById("countdown").innerHTML = "¡Hoy es el gran día!";
    return;
  }
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  document.getElementById("countdown").innerHTML =
    days + " días, " + hours + " hrs, " + minutes + " min, " + seconds + " seg";
}
setInterval(updateCountdown, 1000);
updateCountdown();