import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Docenti() {
  const [docenti, setDocenti] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const fetchDocenti = async () => {
      try {
        const res = await axios.get('/api/docenti');
        setDocenti(res.data);
      } catch (err) {
        setErrore('Errore nel caricamento dei docenti');
      } finally {
        setLoading(false);
      }
    };
    fetchDocenti();
  }, []);

  if (loading) return <p>Caricamento docenti…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Docenti</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Cognome</th>
            <th>Nome</th>
            <th>Materia</th>
          </tr>
        </thead>
        <tbody>
          {docenti.map((d) => (
            <tr key={d.id}>
              <td>{d.cognome}</td>
              <td>{d.nome}</td>
              <td>{d.materia}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Docenti;

