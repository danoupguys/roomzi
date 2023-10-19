const popup = document.getElementById("Login-popup-container");

function openPopup() {
    popup.classList.remove("hidden");
    popup.classList.add("flex");
}

function closePopup(event) {
    if (event.currentTarget === event.target) {
        popup.classList.remove("flex");
        popup.classList.add("hidden");
    }
}
