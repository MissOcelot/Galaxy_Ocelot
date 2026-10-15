
const scriptUrl = document.currentScript.src;
const scriptFolder = new URL(".", scriptUrl);
const clickSound = new Audio(
    new URL("clickk.mp3", scriptFolder).href
);

document.addEventListener("click", function(event) {
    const clickable = event.target.closest(
        "button, a.text-button, a.image-button"
    );

    if (!clickable) return;

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

        clickSound.currentTime = 0.06;
        clickSound.play().catch(() => {});

        const destination = clickable.href;

        setTimeout(function() {
            window.location.href = destination;
        }, 150);
    } else {
        clickSound.currentTime = 0.06;
        clickSound.play().catch(() => {});
    }
});
