document.querySelectorAll('.product-checkbox').forEach(checkbox => {
    const row = checkbox.closest('tr');
    const quantityCell = row.querySelector('.quantity-cell');
    const discountCell = row.querySelector('.discount-cell');
    const quantityInput = row.querySelector('.quantity-input');
    const discountInput = row.querySelector('.discount-input');

    function updateValue() {
        const data = {
        codigo: checkbox.dataset.codigo,
        nombre: checkbox.dataset.nombre,
        descripcion_producto: checkbox.dataset.descripcion,
        precio_unitario: parseFloat(checkbox.dataset.precio_unitario),
        impuesto_adicional: (checkbox.dataset.impuesto_adicional && checkbox.dataset.impuesto_adicional !== 'None') ? checkbox.dataset.impuesto_adicional : null,
        descripcion_impuesto_adicional: checkbox.dataset.descripcion_impuesto_adicional,
        alicuota: (checkbox.dataset.alicuota && checkbox.dataset.alicuota !== 'None') ? checkbox.dataset.alicuota : null,
        cantidad: parseInt(quantityInput.value) || 1,
        porcentaje_bonificado: parseFloat(discountInput.value) || 0
        };
        checkbox.value = JSON.stringify(data);
    }

    checkbox.addEventListener('change', () => {
        if (checkbox.checked) {
        quantityCell.style.display = 'table-cell';
        discountCell.style.display = 'table-cell';
        } else {
        quantityCell.style.display = 'none';
        discountCell.style.display = 'none';
        }
        updateValue();
    });

    quantityInput.addEventListener('input', updateValue);
    discountInput.addEventListener('input', updateValue);

    if (checkbox.checked) {
        quantityCell.style.display = 'table-cell';
        discountCell.style.display = 'table-cell';
    } else {
        quantityCell.style.display = 'none';
        discountCell.style.display = 'none';
    }
    updateValue();
});

/*Revisa si se usa consumidor final*/
document.addEventListener("DOMContentLoaded", function () {
    const tipo_doc = document.getElementById("tipo_doc");

    const texto_nro_doc = document.getElementById("texto_nro_doc");
    const nro_doc_content = document.getElementById("numero_doc_cliente");

    const texto_nombre_apellido = document.getElementById("texto_nombre_apellido");
    const nombre_apellido_cliente = document.getElementById("nombre_apellido_cliente");

    function toggleDocFields() {
        const valor = tipo_doc.value;
        const mostrar = (valor !== "CONSUMIDOR FINAL");

        texto_nro_doc.style.display = mostrar ? "block" : "none";
        nro_doc_content.required = mostrar;

        texto_nombre_apellido.style.display = mostrar ? "block" : "none";
        nombre_apellido_cliente.required = mostrar;
    }
    tipo_doc.addEventListener("change", toggleDocFields);
    toggleDocFields();

});

/*Revisa si el tipo de Factura usado*/
document.addEventListener("DOMContentLoaded", function () {
    const tipo_doc = document.getElementById("tipo_factura");

    const nro_telefono = document.getElementById("numero_telefono");
    const texto_nro_telefono = document.getElementById("texto_nro_telefono");

    const texto_provincia = document.getElementById("texto_provincia");
    const provincia = document.getElementById("provincia");

    const texto_localidad = document.getElementById("texto_localidad");
    const localidad = document.getElementById("localidad");

    const texto_domicilio = document.getElementById("texto_domicilio");
    const domicilio = document.getElementById("domicilio");
    
    function toggleDocFields() {
        const valor = tipo_doc.value;
        const factura_A = (valor == "Factura A");
        const factura_B = (valor == "Factura B");

        if (factura_A){
            nro_telefono.classList.remove("hidden");
            nro_telefono.required = true;

            texto_nro_telefono.classList.remove("hidden");
            texto_nro_telefono.required = true;

            texto_provincia.classList.remove("hidden");
            texto_provincia.required = true;

            provincia.classList.remove("hidden");
            provincia.required = true;

            texto_localidad.classList.remove("hidden");
            texto_localidad.required = true;

            localidad.classList.remove("hidden");
            localidad.required = true;

            texto_domicilio.classList.remove("hidden");
            texto_domicilio.required = true;

            domicilio.classList.remove("hidden");
            domicilio.required = true;
        }
        else{
            nro_telefono.classList.add("hidden");
            nro_telefono.required = false;

            texto_nro_telefono.classList.add("hidden");
            texto_nro_telefono.required = false;

            texto_provincia.classList.add("hidden");
            texto_provincia.required = false;

            provincia.classList.add("hidden");
            provincia.required = false;

            texto_localidad.classList.add("hidden");
            texto_localidad.required = false;

            localidad.classList.add("hidden");
            localidad.required = false;

            if(factura_B){
                texto_domicilio.classList.remove("hidden");
                texto_domicilio.required = true;

                domicilio.classList.remove("hidden");
                domicilio.required = true;
            }
            else{
                texto_domicilio.classList.add("hidden");
                texto_domicilio.required = false;

                domicilio.classList.add("hidden");
                domicilio.required = false;
            }
        }
    }

    tipo_doc.addEventListener("change", toggleDocFields);

    toggleDocFields();
});

document.addEventListener("DOMContentLoaded", function () {
    const conceptoSelect = document.getElementById("concepto");

    const fechaDesdeCont = document.getElementById("campo_fecha_desde");
    const fechaHastaCont = document.getElementById("campo_fecha_hasta");
    const fechaVtoCont = document.getElementById("campo_fecha_vto_pago");

    const fechaDesde = document.getElementById("fecha_desde");
    const fechaHasta = document.getElementById("fecha_hasta");
    const fechaVto = document.getElementById("fecha_vto_pago");

    function toggleFechaFields() {
    const valor = conceptoSelect.value;
    const mostrar = (valor === "SERVICIOS" || valor === "PRODUCTOS Y SERVICIOS");

    fechaDesdeCont.style.display = mostrar ? "block" : "none";
    fechaHastaCont.style.display = mostrar ? "block" : "none";
    fechaVtoCont.style.display = mostrar ? "block" : "none";

    fechaDesde.required = mostrar;
    fechaHasta.required = mostrar;
    fechaVto.required = mostrar;
    }

    conceptoSelect.addEventListener("change", toggleFechaFields);

    toggleFechaFields();
});





document.addEventListener("DOMContentLoaded", function () {
    const radios = document.querySelectorAll(".cliente-radio");

    const tipoDocSelect = document.getElementById("tipo_doc");
    const nroDocInput = document.getElementById("numero_doc_cliente");
    const nombreInput = document.getElementById("nombre_apellido_cliente");
    const telefonoInput = document.getElementById("numero_telefono");
    const provinciaInput = document.getElementById("provincia");
    const localidadInput = document.getElementById("localidad");
    const domicilioInput = document.getElementById("domicilio");
    const conceptoIvaSelect = document.getElementById("concepto_iva");

    radios.forEach(radio => {
        radio.addEventListener("change", function () {
            if (!this.checked) return;

            const nombre = this.dataset.nombre || "";
            const tipoDoc = this.dataset.tipoDoc || "DNI";
            const numDoc = this.dataset.numDoc || "";
            const telefono = this.dataset.telefono || "";
            const provincia = this.dataset.provincia || "";
            const localidad = this.dataset.localidad || "";
            const domicilio = this.dataset.domicilio || "";
            const condicionIva = this.dataset.condicionIva || "";

            // Rellenar campos
            nombreInput.value = nombre;
            nroDocInput.value = numDoc;
            telefonoInput.value = telefono;
            provinciaInput.value = provincia;
            localidadInput.value = localidad;
            domicilioInput.value = domicilio;

            // Tipo de documento
            setSelectValue(tipoDocSelect, tipoDoc);

            // Condición IVA
            setSelectValue(conceptoIvaSelect, condicionIva);

            // Disparar eventos para que se apliquen tus validaciones actuales
            tipoDocSelect.dispatchEvent(new Event("change"));
            conceptoIvaSelect.dispatchEvent(new Event("change"));
        });
    });

    function setSelectValue(selectElement, value) {
        for (let i = 0; i < selectElement.options.length; i++) {
            if (selectElement.options[i].value.toLowerCase() === value.toLowerCase()) {
                selectElement.selectedIndex = i;
                return;
            }
        }
    }
});

document.getElementById("tipo_factura").addEventListener("change", function () {
    const tipoFactura = this.value;
    const tipoDocSelect = document.getElementById("tipo_doc");
    const conceptoIvaSelect = document.getElementById("concepto_iva");

    // Resetear todo primero
    Array.from(tipoDocSelect.options).forEach(opt => opt.disabled = false);
    Array.from(conceptoIvaSelect.options).forEach(opt => opt.disabled = false);

    if (tipoFactura === "Factura A") {
        Array.from(tipoDocSelect.options).forEach(opt => {
            opt.disabled = opt.value !== "CUIT";
        });
        tipoDocSelect.value = "CUIT";

        // Solo Responsable Inscripto
        Array.from(conceptoIvaSelect.options).forEach(opt => {
            opt.disabled = opt.value !== "Responsable Inscripto";
        });
        conceptoIvaSelect.value = "Responsable Inscripto";

    } else if (tipoFactura === "Factura B") {
        // --- Tipo Documento ---
        if (!tipoDocSelect.value) {
            tipoDocSelect.value = "DNI";
        }

        // --- Condición IVA ---
        Array.from(conceptoIvaSelect.options).forEach(opt => {
            if (opt.value === "Responsable Inscripto") {
                opt.disabled = true;
            }
        });

        if (conceptoIvaSelect.value === "Responsable Inscripto") {
            conceptoIvaSelect.value = "Consumidor Final";
        }
    }
});