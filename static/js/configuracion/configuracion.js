function changeContent(toggleId) {
    // Oculta todos los contenidos
    const contents = document.querySelectorAll('.content-item');
    contents.forEach(content => content.style.display = 'none');

    // Muestra el contenido correspondiente al toggle seleccionado
    const selectedContent = document.getElementById(`content-${toggleId}`);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }
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