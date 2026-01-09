function changeContent(toggleId) {
    const contents = document.querySelectorAll('.content-item');
    contents.forEach(content => content.style.display = 'none');

    const selectedContent = document.getElementById(`content-${toggleId}`);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }
}

function mostrarLoader(event) {
    setTimeout(() => {
        const loader = document.querySelector(".loader");

        loader.classList.remove("loader-hidden");
        document.body.style.overflow = "hidden";
        document.body.style.pointerEvents = "none";
    }, 5000);
}

function mostrarExito(event_) {
    const pantalla = document.querySelector(".pantalla_exito");
    const mensaje = document.getElementById("mensaje_exito");
    const formulario = document.getElementById("formulario_exito");

    pantalla.classList.remove("pantalla_exito-hidden");
    document.body.style.overflow = "hidden";
    mensaje.textContent = "Descargando...";
    mensaje.style.color = "#f1f7fd"; 
    setTimeout(() => {
        mensaje.textContent = "Descarga Exitosa";
        formulario.style.display = "block";
    }, 3000);
}

function mostrarLoader(event) {
    event.target.submit();
}

function mostrarAgregar(eventA) {
    const loader = document.getElementById("agregar");

    loader.classList.remove("accion_item-hidden");

    document.body.style.overflow = "hidden";
}

function mostrarModificar(eventM) {
    const loader = document.getElementById("modificar");

    loader.classList.remove("accion_item-hidden");

    document.body.style.overflow = "hidden";
}

function mostrarEliminar(eventE) {
    const loader = document.getElementById("eliminar");

    loader.classList.remove("accion_item-hidden");

    document.body.style.overflow = "hidden";
}

document.addEventListener("DOMContentLoaded", function () {
    const content1 = document.getElementById("content-1");

    const iagSelect = content1.querySelector("#concepto");
    const iagExtraFields = content1.querySelector("#concepto_extra");
    const descripcionInput = content1.querySelector('input[name="d_i_a"]');
    const alicuotaInput = content1.querySelector('input[name="alicuota"]');

    function toggleFields() {
        const mostrar = iagSelect.value !== "";

        iagExtraFields.style.display = mostrar ? "block" : "none";
        descripcionInput.required = mostrar;
        alicuotaInput.required = mostrar;
    }

    iagSelect.addEventListener("change", toggleFields);
    toggleFields(); // aplica en caso de valor ya cargado
});

function filterItems() {
    let searchQuery = document.getElementById("search-box").value.toLowerCase();
    let rows = document.querySelectorAll("table tbody tr");

    rows.forEach(row => {
        // Usar data-name si existe, si no usar texto de la fila
        const input = row.querySelector("input.product-checkbox");
        const name = input?.getAttribute("data-name")?.toLowerCase() ?? "";

        // También considerar todo el texto visible
        const rowText = row.textContent.toLowerCase();

        if (name.includes(searchQuery) || rowText.includes(searchQuery)) {
            row.style.display = "table-row";
        } else {
            row.style.display = "none";
        }
    });
}