function filterItems(sectionId) {
    let search = document.getElementById(`search-box-${sectionId}`).value.toLowerCase();
    let rows = document.querySelectorAll(`#items-container-${sectionId} tr.checkbox`);
    rows.forEach(row => {
        let name = row.dataset.name.toLowerCase();
        row.style.display = name.includes(search) ? '' : 'none';
    });
}

function mostrarExito1(event_) {
    const pantalla = document.querySelector(".pantalla_exito");
    const mensaje = document.getElementById("mensaje_exito");
    const formulario = document.getElementById("formulario_exito");

    pantalla.classList.remove("pantalla_exito-hidden");
    document.body.style.overflow = "hidden";
    mensaje.textContent = "Armando PDF...";
    mensaje.style.color = "#f1f7fd"; 

    setTimeout(() => {
        mensaje.textContent = "PDF Exitoso";
        mensaje.style.color = "#f1f7fd"; 
        formulario.style.display = "block";
    }, 10000);
}

function mostrarExito2(event_) {
    const pantalla = document.querySelector(".pantalla_exito");
    const mensaje = document.getElementById("mensaje_exito");
    const formulario = document.getElementById("formulario_exito");

    pantalla.classList.remove("pantalla_exito-hidden");
    document.body.style.overflow = "hidden";
    mensaje.textContent = "Armando nota de crédito...";
    mensaje.style.color = "#f1f7fd"; 

    setTimeout(() => {
        mensaje.textContent = "Nota Exitosa";
        mensaje.style.color = "#f1f7fd"; 
        formulario.style.display = "block";
    }, 10000);
}

function mostrarLoader(event) {
    event.target.submit();
}

function changeContent(toggleId) {
    const contents = document.querySelectorAll('.content-item');
    contents.forEach(content => content.style.display = 'none');

    const selectedContent = document.getElementById(`content-${toggleId}`);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const filas = document.querySelectorAll("tr.checkbox");

    filas.forEach(fila => {
        const identificador = fila.getAttribute("data-name");

        if (!identificador || identificador.trim() === "") {
            const boton = fila.querySelector("button");

            if (boton) {
                boton.disabled = true;
                boton.style.opacity = "0.0";
                boton.style.cursor = "not-allowed";
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const filas = document.querySelectorAll("#items-container-facturas tr.checkbox");

    filas.forEach(fila => {
        const celdas = fila.querySelectorAll("td");

        if (celdas.length > 2) {
            let tipoFacturaNota = celdas[2].innerText
                .toLowerCase()
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g, "")
                .trim();

            if (tipoFacturaNota.includes("nota")) {
                const boton = fila.querySelector("button");

                if (boton) {
                    boton.disabled = true;
                    boton.style.opacity = "0.4";
                    boton.style.cursor = "not-allowed";
                }
            }
        }
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const filas = document.querySelectorAll("#items-container-2 tbody tr");

    filas.forEach(fila => {
        const celdas = fila.querySelectorAll("td");

        const INDEX_CAE_VTO = 43; // ← ESTE ES EL CORRECTO PARA TU TABLA

        if (!celdas[INDEX_CAE_VTO]) return;

        const textoFecha = celdas[INDEX_CAE_VTO].innerText.trim();

        if (!textoFecha || !/^\d{8}$/.test(textoFecha)) return;

        const año = parseInt(textoFecha.substring(0, 4));
        const mes = parseInt(textoFecha.substring(4, 6)) - 1;
        const dia = parseInt(textoFecha.substring(6, 8));

        const fechaVto = new Date(año, mes, dia);
        const hoy = new Date();

        hoy.setHours(0,0,0,0);
        fechaVto.setHours(0,0,0,0);

        const diffDias = (fechaVto - hoy) / (1000 * 60 * 60 * 24);

        const boton = fila.querySelector("button");

        if (diffDias >= 15) {
            boton.disabled = true;
            boton.classList.add("btn-secondary");
            boton.title = "No se puede hacer nota de crédito: fuera del plazo legal (15 días)";
        }
    });
});