
const music = document.getElementById("background-music");
const musicToggle = document.getElementById("music-toggle");
const musicIcon = document.getElementById("music-icon");

musicToggle.addEventListener("click", async function() {
    if (music.paused) {
        try {
            await music.play();
            musicIcon.src = "../home/musicon.png";
        } catch (error) {
            console.error("Music playback failed:", error);
            musicToggle.textContent = "Music didn't play :(. Reload and try again";
        }
    } else {
        music.pause();
        musicIcon.src ="../home/musicoff.png"
    }
});
