const popup = document.getElementById("Login-popup-container")

function openPopup() {
    popup.classList.remove("hidden")
}

function closePopup(params) {

    console.log(params.target)
    if (params.target.id === "Login-popup-container" || params.target.id === "enter-btn") {
        popup.classList.add("hidden")
    }
}