function mostrarLoader(event) {
    const loader = document.querySelector(".loader");

    loader.classList.remove("loader-hidden");

    document.body.style.overflow = "hidden";
    document.body.style.pointerEvents = "none";
}