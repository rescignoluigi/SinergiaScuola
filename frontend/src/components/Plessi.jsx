import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Plessi() {
  const [plessi, setPlessi] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const fetchPlessi = async () => {
      try {
        const res = await axios.get('/api/plessi');
        setPlessi(res.data);
      } catch (err) {
        setErrore('Errore nel caricamento dei plessi');
      } finally {
        setLoading(false);
      }
    };
    fetchPlessi();
  }, []);

  if (loading) return <p>Caricamento plessi…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Plessi</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Codice</th>
            <th>Nome</th>
            <th>Indirizzo</th>
          </tr>
        </thead>
        <tbody>
          {plessi.map((p) => (
            <tr key={p.id || p.codice}>
              <td>{p.codice}</td>
              <td>{p.nome}</td>
              <td>{p.indirizzo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Plessi;

