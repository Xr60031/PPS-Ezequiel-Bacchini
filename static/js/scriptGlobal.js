// Función para eliminar el mensaje flash al hacer clic en el botón
function deleteMessage() {
    fetch("/delete_message", {
        method: "POST",  // Enviar la solicitud como POST
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        if (data.success) {
            // Eliminar el mensaje flash del DOM sin recargar la página
            document.getElementById('flash-message').style.display = 'none';
        }
    });
}