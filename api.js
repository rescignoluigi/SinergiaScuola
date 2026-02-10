const API_URL = "https://script.google.com/macros/s/AKfycby8xjqBRJTkghkEmRh07dLC0AXRLWSSChO_yHn6JEypwL2YFOAGFu1hqUImE4qMOVmT/exec";

async function callApi(action, data = {}) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, ...data })
    });

    return await response.json();

  } catch (err) {
    console.error("Errore API:", err);
    return { ok: false, error: err.message };
  }
}

async function inserisciAssenza(dati) {
  return await callApi("inserisciAssenza", { data: dati });
}

async function elencoAssenzeGiornaliere(dataIso) {
  return await callApi("elencoAssenzeGiornaliere", { data: dataIso });
}

async function proponiSostituzioni(idAssenza) {
  return await callApi("proponiSostituzioni", { idAssenza });
}

async function confermaSostituzione(dati) {
  return await callApi("confermaSostituzione", { data: dati });
}
