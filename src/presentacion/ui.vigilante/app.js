const estado = document.getElementById("estado");

async function cargarModo() {
    try {
        const resp = await fetch("http://127.0.0.1:8000/porton/estado");
        const data = await resp.json();
        document.getElementById("modoInfo").textContent =
            `Modo actual: ${data.modo}`;
    } catch (error) {
        document.getElementById("modoInfo").textContent =
            "No se pudo detectar el modo";
    }
}

cargarModo(); // ← Ejecutar al cargar


async function llamarAPI(ruta) {
    try {
        const respuesta = await fetch(`http://127.0.0.1:8000${ruta}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });

        const datos = await respuesta.json();
        estado.textContent = `Estado: ${datos.mensaje}`;
    } catch (error) {
        estado.textContent = "Error conectando con el servidor";
    }
}

document.getElementById("btnAbrir").addEventListener("click", () => {
    llamarAPI("/porton/abrir");
});

document.getElementById("btnCerrar").addEventListener("click", () => {
    llamarAPI("/porton/cerrar");
});
