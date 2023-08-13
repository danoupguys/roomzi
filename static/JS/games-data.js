const gamesDataChilds = document.querySelectorAll("#games-data-container > *");
const gamesDataToggles = document.getElementById("games-data-toggles");

gamesDataToggles.addEventListener("click", (e) => {
    if (e.target.tagName === "LI") {
        const target = document.querySelector(e.target.dataset.targetId);
        const toggles = document.querySelectorAll("#games-data-toggles > li");

        toggles.forEach((toggle) => {
            if (toggle === e.target) toggle.className = "mx-3 cursor-pointer border-b-2 border-b-inherit drop-shadow-[0_0_3px_#F00] pb-3 hover:drop-shadow-[0_0_3px_#F00] hover:border-b-inherit";
            else toggle.className = "mx-3 cursor-pointer border-b-2 border-b-transparent pb-3 hover:drop-shadow-[0_0_3px_#F00] hover:border-b-inherit";
        })

        gamesDataChilds.forEach((child) => {
            if (child.id !== target.id) child.classList.add("hidden");
            else child.classList.remove("hidden");
        });
    }
});
