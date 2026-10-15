
const clickSound = new Audio("clickk.mp3");

document.addEventListener("click", function(event) {
    const clickable = event.target.closest(
        "button, a.text-button, a.image-button"
    );

    if (!clickable) return;

    // Let modified clicks behave normally (Ctrl-click, new tab, etc.).
    const isNormalLinkClick =
        clickable.matches("a") &&
        event.button === 0 &&
        !event.ctrlKey &&
        !event.metaKey &&
        !event.shiftKey &&
        !event.altKey &&
        clickable.target !== "_blank";

    if (isNormalLinkClick) {
        event.preventDefault();

        clickSound.currentTime = 0.05;
        clickSound.play().catch(() => {});

        const destination = clickable.href;

        // Give the sound a moment to start before navigating.
        setTimeout(function() {
            window.location.href = destination;
        }, 150);
    } else {
        clickSound.currentTime = 0.05;
        clickSound.play().catch(() => {});
    }
});
