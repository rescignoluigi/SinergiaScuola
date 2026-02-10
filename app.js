/************************************************************
 *  GESTIONE FORM ASSENZE
 ************************************************************/
if (document.getElementById("formAssenza")) {
  document.getElementById("formAssenza").addEventListener("submit", async (e) => {
    e.preventDefault();

    const dati = {
      data: document.getElementById("data").value,
      idDocente: document.getElementById("idDocente").value,
      cognomeDocente: document.getElementById("cognome").value,
      nomeDocente: document.getElementById("nome").value,
      oraDa: document.getElementById("oraDa").value,
      oraA: document.getElementById("oraA").value,
      tipo: document.getElementById("tipo").value,
      note: document.getElementById("note").value
    };

    const risposta = await inserisciAssenza(dati);

    document.getElementById("risultato").innerHTML =
      risposta.ok
        ? `<p style="color:green">Assenza registrata. ID: ${risposta.idAssenza}</p>`
        : `<p style="color:red">Errore: ${risposta.error}</p>`;
  });
}

/************************************************************
 *  PROPOSTE SOSTITUZIONI
 ************************************************************/
async function cercaProposte() {
  const id = document.getElementById("idAssenza").value;
  const r = await proponiSostituzioni(id);

  if (!r.ok) {
    document.getElementById("proposte").innerHTML =
      `<p style="color:red">${r.error}</p>`;
    return;
  }

  let html = `<h4>Docenti disponibili:</h4><ul>`;
  r.proposte.forEach(p => {
    html += `<li>${p.cognome} ${p.nome} (${p.materia}) — ${p.plesso}</li>`;
  });
  html += `</ul>`;

  document.getElementById("proposte").innerHTML = html;
}

/************************************************************
 *  CONFERMA SOSTITUZIONE
 ************************************************************/
if (document.getElementById("formSostituzione")) {
  document.getElementById("formSostituzione").addEventListener("submit", async (e) => {
    e.preventDefault();

    const dati = {
      idAssenza: document.getElementById("idAssenzaConf").value,
      ora: document.getElementById("ora").value,
      idDocenteSostituto: document.getElementById("idDocenteSost").value,
      classe: document.getElementById("classe").value,
      aula: document.getElementById("aula").value,
      note: document.getElementById("noteSost").value
    };

    const r = await confermaSostituzione(dati);

    document.getElementById("risultato").innerHTML =
      r.ok
        ? `<p style="color:green">Sostituzione confermata. ID: ${r.idSostituzione}</p>`
        : `<p style="color:red">Errore: ${r.error}</p>`;
  });
}
