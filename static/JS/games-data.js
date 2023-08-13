const gamesDataChilds = document.querySelectorAll("#games-data-container > *");
const gamesDataToggles = document.getElementById("games-data-toggles");

gamesDataToggles.addEventListener("click", (e) => {
    if (e.target.tagName === "LI") {
        const target = document.querySelector(e.target.dataset.targetId);

        gamesDataChilds.forEach((child) => {
            if (child.id !== target.id) child.classList.add("hidden");
            else child.classList.remove("hidden");
        });
    }
});
