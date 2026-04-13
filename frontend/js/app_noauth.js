const API_BASE_URL = "https://sinergiascuola-backend-192075040354.europe-west1.run.app";

async function registerInstitute() {
    const schoolName = document.getElementById("schoolName").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_BASE_URL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ schoolName, email, password })
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result);
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result);
}
