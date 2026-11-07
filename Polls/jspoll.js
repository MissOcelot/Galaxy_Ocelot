const form = document.getElementById("poll-form");
const results = document.getElementById("results");

const previousVote = localStorage.getItem("chname1");

if (previousVote) {
    results.textContent = "You already picked " + previousVote + "!";
    form.querySelector("button[type='submit']").disabled = true;
}


form.addEventListener("submit", function(event) {
    event.preventDefault()
    const choice = document.querySelector('input[name="chname"]:checked').value;
    localStorage.setItem("chname1", choice);
    document.getElementById("results").textContent =
        choice + "? Nice choice! Your answer was sent to Ocelot.";
    form.querySelector("button[type='submit']").disabled = true;
});