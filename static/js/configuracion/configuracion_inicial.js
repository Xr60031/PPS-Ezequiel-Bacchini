function redirectAfterSubmit() {
    setTimeout(function() {
        window.location.href = "/menu_facturador";
    }, 5000);
}
function mostrarLoader(event) {
    const loader = document.querySelector(".loader");

    loader.classList.remove("loader-hidden");

    document.body.style.overflow = "hidden";
    document.body.style.pointerEvents = "none";
}

document.addEventListener("DOMContentLoaded", function () {
    const iagSelect = document.getElementById("iag");
    const iagExtraFields = document.getElementById("iag_extra");
    const descripcionInput = document.querySelector('input[name="d_iag"]');
    const alicuotaInput = document.querySelector('input[name="alicuota"]');

    function toggleFields() {
    const mostrar = iagSelect.value !== "";

    iagExtraFields.style.display = mostrar ? "block" : "none";
    descripcionInput.required = mostrar;
    alicuotaInput.required = mostrar;
    }

    iagSelect.addEventListener("change", toggleFields);
});