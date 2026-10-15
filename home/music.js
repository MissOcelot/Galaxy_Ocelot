
const music = document.getElementById("background-music");
const musicToggle = document.getElementById("music-toggle");

musicToggle.addEventListener("click", async function() {
    if (music.paused) {
        try {
            await music.play();
            musicToggle.textContent = "Stop music";
        } catch (error) {
            console.error("Music playback failed:", error);
            musicToggle.textContent = "Music failed. Reload and try  again";
        }
    } else {
        music.pause();
        musicToggle.textContent = "Music again";
    }
});
