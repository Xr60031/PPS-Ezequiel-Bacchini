document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById('toggleTheme');

    const temaOscuro = {
        '--color-principal': '#70b1ea',
        '--color-secundario': '#4a90e2',
        '--color-fondo': '#1d2c4e',

        '--barranav': '#2d51a0',
        '--barranav-boton': '#3978d7',
        '--barranav-hover': '#70b1ea',
        '--barranav-text': '#f1f7fd',
        '--barranav-hover-text': '#ffffff',
        '--barranav-borde': '#4a90e2',

        '--boton': '#29467f',
        '--boton-hover': '#3978d7',
        '--boton-text': '#f1f7fd',
        '--boton-hover-text': '#ffffff',
        '--boton-borde': '#70b1ea',

        '--marco': '#2d3e5c',
        '--marco-shadow': '#1d2c4e',

        '--color-letra-h1': '#c6e0f7',
        '--color-letra-hx': '#9ecdf2',
        '--color-parrafo': '#f1f7fd',
    };

    let temaActual = localStorage.getItem('tema') || 'blanco';

    if (temaActual === 'oscuro') {
        for (let variable in temaOscuro) {
            document.documentElement.style.setProperty(variable, temaOscuro[variable]);
        }
    }

    toggleButton.addEventListener('click', function(e) {
        e.preventDefault();
        const root = document.documentElement;

        if (temaActual === 'blanco') {
            for (let variable in temaOscuro) {
                root.style.setProperty(variable, temaOscuro[variable]);
            }
            temaActual = 'oscuro';
        } else {
            for (let variable in temaOscuro) {
                root.style.removeProperty(variable);
            }
            temaActual = 'blanco';
        }

        localStorage.setItem('tema', temaActual);
    });
});
