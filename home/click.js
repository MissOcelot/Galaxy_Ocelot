const clickSound = new Audio("click.mp3");

document.addEventListener("click", function(event) {
    const button = event.target.closest("button");

    if (button) {
        clickSound.currentTime = 0;
        clickSound.play();
    }
});