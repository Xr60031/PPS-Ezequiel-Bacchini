function mostrarExito(event_) {
            const pantalla = document.querySelector(".pantalla_exito");
            const mensaje = document.getElementById("mensaje_exito");
            const formulario = document.getElementById("formulario_exito");

            pantalla.classList.remove("pantalla_exito-hidden");
            document.body.style.overflow = "hidden";
            mensaje.textContent = "Facturando...";

            setTimeout(() => {
                mensaje.textContent = "Facturación Exitosa";
                formulario.style.display = "block";
            }, 10000);
        }

        function mostrarLoader(event) {
            event.target.submit();
        }