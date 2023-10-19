const gamesSlider = document.getElementById("games-carousel");

if (gamesSlider) {
    switch (true) {
        case window.matchMedia("(min-width: 1280px)").matches:
            gamesSlider.dataset.carouselItems = "7";
            break;

        case window.matchMedia("(min-width: 1024px)").matches:
            gamesSlider.dataset.carouselItems = "5";
            break;

        case window.matchMedia("(min-width: 768px)").matches:
            gamesSlider.dataset.carouselItems = "4";
            break;

        case window.matchMedia("(min-width: 640px)").matches:
            gamesSlider.dataset.carouselItems = "3";
            break;

        default:
            gamesSlider.dataset.carouselItems = "2";
    }
}
