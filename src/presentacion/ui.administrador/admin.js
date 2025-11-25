const URL = "http://127.0.0.1:8000/porton/historial";
const tabla = document.getElementById("tablaHistorial");
const btnRecargar = document.getElementById("recargar");

// Cargar historial al iniciar
cargarHistorial();

btnRecargar.addEventListener("click", cargarHistorial);

async function cargarHistorial() {
    tabla.innerHTML = `
        <tr>
            <td colspan="3" class="loading">Cargando datos...</td>
        </tr>
    `;

    try {
        const res = await fetch(URL);
        const data = await res.json();

        tabla.innerHTML = ""; // limpiar

        data.forEach(evento => {
            const fila = `
                <tr>
                    <td>${evento.accion}</td>
                    <td>${evento.mensaje}</td>
                    <td>${formatearFecha(evento.fecha)}</td>
                </tr>
            `;
            tabla.innerHTML += fila;
        });

    } catch (error) {
        tabla.innerHTML = `
            <tr>
                <td colspan="3" class="loading">Error al cargar datos</td>
            </tr>
        `;
    }
}

function formatearFecha(fechaISO) {
    const fecha = new Date(fechaISO);
    return fecha.toLocaleString("es-CO");
}
