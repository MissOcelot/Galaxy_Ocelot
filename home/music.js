const music = document.getElementById("background-music");
const musicToggle = document.getElementById("music-toggle");

if (music && musicToggle) {
    music.volume = 0.5;

    musicToggle.addEventListener("click", async function() {
        if (music.paused) {
            try {
                await music.play();
                musicToggle.textContent = "♫ Pause music";
            } catch (error) {
                musicToggle.textContent = "♫ Try playing again";
            }
        } else {
            music.pause();
            musicToggle.textContent = "♫ Play music";
        }
    });
}
