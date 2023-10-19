const navToggle = document.getElementById("nav-toggle");

const mobileNav = document.getElementById("mobile-nav");
const mobileNavMenu = document.getElementById("mobile-nav-menu");
const mobileNavContainer = document.getElementById("mobile-nav-container");

navToggle.addEventListener("click", () => {
    mobileNavContainer.classList.remove("hidden");

    setTimeout(() => {
        mobileNavMenu.style.right = "0px";
    }, 200);
});

mobileNav.addEventListener("click", (event) => {
    if (event.currentTarget === event.target) {
        mobileNavMenu.style.right = "";

        setTimeout(() => {
            mobileNavContainer.classList.add("hidden");
        }, 500);
    }
});
