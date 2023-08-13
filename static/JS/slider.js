const carouselControls = document.querySelectorAll("[data-slide]");

carouselControls.forEach((control) => {
    control.addEventListener("click", () => {
        const carouselId = control.dataset.carouselTarget;
        const carousel = document.querySelector(carouselId);

        const direction = control.dataset.slide;
        const carouselWidth = carousel.scrollWidth;
        const eachScrollItems = carousel.dataset.carouselItems;
        const eachCarouselWidth = Math.ceil(carouselWidth / carousel.children.length) * eachScrollItems;
        const scrollWidth = direction === "next" ? eachCarouselWidth : -eachCarouselWidth;

        if (carousel.scrollLeft + scrollWidth >= carouselWidth) {
            carousel.scroll({ behavior: "smooth", left: 0, top: 0 });
        } else if (carousel.scrollLeft === 0 && direction === "prev") {
            carousel.scroll({ behavior: "smooth", left: carouselWidth, top: 0 });
        } else {
            carousel.scrollBy({ behavior: "smooth", left: scrollWidth, top: 0 });
        }
    });
});
