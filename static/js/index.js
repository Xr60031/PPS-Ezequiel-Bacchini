function aceptarCookies() {
    document.cookie = "cookies_aceptadas=true; path=/; max-age=" + 60 * 60 * 24 * 365 * 100;
    document.getElementById('cookie-modal').style.display = 'none';
    document.getElementById('cookie-overlay').style.display = 'none';
}

function mostrarModalSiEsNecesario() {
    if (!document.cookie.includes("cookies_aceptadas=true")) {
        document.getElementById('cookie-modal').style.display = 'block';
        document.getElementById('cookie-overlay').style.display = 'block';
    }
}

window.onload = mostrarModalSiEsNecesario;