function filterItems(sectionId) {
    let search = document.getElementById(`search-box-${sectionId}`).value.toLowerCase();
    let rows = document.querySelectorAll(`#items-container-${sectionId} tr.checkbox`);
    rows.forEach(row => {
        let name = row.dataset.name.toLowerCase();
        row.style.display = name.includes(search) ? '' : 'none';
    });
}

function mostrarExito(event_) {
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

window.onload = function() {
    const filas = document.querySelectorAll('tr.checkbox');
    const facturas = [];
    const clavesNotasCredito = new Set();

    filas.forEach((fila, idx) => {
        const clave = fila.getAttribute('data-name') || '';
        let tipoTexto = '';

        // Buscamos en todas las celdas el texto "factura" o "nota de crédito"
        for(let i=0; i < fila.cells.length; i++) {
            const texto = fila.cells[i].textContent.toLowerCase();
            if (texto.includes('nota de crédito')) {
                tipoTexto = 'nota de crédito';
                break;
            } else if (texto.includes('factura')) {
                tipoTexto = 'factura';
                // No break, por si hay nota después en otra celda (pero asumimos primera que encuentre)
            }
        }

        if(tipoTexto === 'nota de crédito') {
            clavesNotasCredito.add(clave);
        } else if (tipoTexto === 'factura') {
            facturas.push({ clave, fila });
        }
    });

    facturas.forEach(({ clave, fila }) => {
        if (clavesNotasCredito.has(clave)) {
            const radio = fila.querySelector('input[type="radio"]');
            if (radio) {
                radio.remove();
            }
        }
    });
};

function changeContent(toggleId) {
    const contents = document.querySelectorAll('.content-item');
    contents.forEach(content => content.style.display = 'none');

    const selectedContent = document.getElementById(`content-${toggleId}`);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }
}

function filterFacturas(sectionId) {
    const search = document.getElementById('search-box-factura').value.toLowerCase();
    document.querySelectorAll(`#${sectionId} tr.checkbox`).forEach(row => {
        const col2 = row.cells[2]?.innerText.trim().toLowerCase() || '';
        row.style.display = col2.includes(search) ? '' : 'none';
    });
}

document.addEventListener('DOMContentLoaded', () => filterFacturas('items-container-facturas'));