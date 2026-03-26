import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Plessi() {
  const [plessi, setPlessi] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  // Form state
  const [codice, setCodice] = useState("");
  const [nome, setNome] = useState("");
  const [indirizzo, setIndirizzo] = useState("");

  // Toast
  const [toast, setToast] = useState(null);

  const showToast = (msg, type = "success") => {
    setToast({ msg, type });
    setTimeout(() => setToast(null), 2500);
  };

  // Carica plessi
  const fetchPlessi = async () => {
    try {
      const res = await axios.get('/api/plessi/');
      setPlessi(res.data);
    } catch (err) {
      setErrore("Errore nel caricamento dei plessi");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPlessi();
  }, []);

  // Aggiungi plesso
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!codice.trim() || !nome.trim() || !indirizzo.trim()) {
      showToast("Compila tutti i campi", "error");
      return;
    }

    try {
      await axios.post('/api/plessi/', {
        codice,
        nome,
        indirizzo
      });

      showToast("Plesso aggiunto con successo");
      setCodice("");
      setNome("");
      setIndirizzo("");

      fetchPlessi();
    } catch (err) {
      showToast("Errore durante l'inserimento", "error");
    }
  };

  // Elimina plesso
  const deletePlesso = async (id) => {
    if (!confirm("Vuoi davvero eliminare questo plesso?")) return;

    try {
      await axios.delete(`/api/plessi/${id}`);
      showToast("Plesso eliminato");
      fetchPlessi();
    } catch (err) {
      showToast("Errore durante l'eliminazione", "error");
    }
  };

  if (loading) return <p>Caricamento plessi…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Plessi</h1>

      {/* TOAST */}
      {toast && (
        <div className={`toast ${toast.type}`}>
          {toast.msg}
        </div>
      )}

      {/* FORM ELEGANTE */}
      <form className="form-card" onSubmit={handleSubmit}>
        <div className="form-row">
          <input
            type="text"
            placeholder="Codice"
            value={codice}
            onChange={(e) => setCodice(e.target.value)}
          />
          <input
            type="text"
            placeholder="Nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
          />
          <input
            type="text"
            placeholder="Indirizzo"
            value={indirizzo}
            onChange={(e) => setIndirizzo(e.target.value)}
          />
          <button type="submit" className="btn-primary">Aggiungi</button>
        </div>
      </form>

      {/* TABELLA */}
      <table className="table">
        <thead>
          <tr>
            <th>Codice</th>
            <th>Nome</th>
            <th>Indirizzo</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {plessi.map((p) => (
            <tr key={p.id}>
              <td>{p.codice}</td>
              <td>{p.nome}</td>
              <td>{p.indirizzo}</td>
              <td>
                <button
                  className="btn-delete"
                  onClick={() => deletePlesso(p.id)}
                >
                  Elimina
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Plessi;


