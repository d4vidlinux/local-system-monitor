async function updateTemp() {
    const response = await fetch("/api/resources");
    const data = await response.json();

    document.getElementById("cpu").textContent = data.cpu + " °C";
    document.getElementById("gpu").textContent = data.gpu + " °C";
    document.getElementById("motherboard").textContent = data.motherboard + " °C";
    document.getElementById("uptime").textContent = data.uptime;
}

updateTemp();
setInterval(updateTemp, 1000);