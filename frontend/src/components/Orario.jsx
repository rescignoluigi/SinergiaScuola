import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Orario() {
  const [righe, setRighe] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const fetchOrario = async () => {
      try {
        const res = await axios.get('/api/orario');
        setRighe(res.data);
      } catch (err) {
        setErrore('Errore nel caricamento dell’orario');
      } finally {
        setLoading(false);
      }
    };
    fetchOrario();
  }, []);

  if (loading) return <p>Caricamento orario…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Orario</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Giorno</th>
            <th>Ora</th>
            <th>Classe</th>
            <th>Docente</th>
            <th>Aula</th>
          </tr>
        </thead>
        <tbody>
          {righe.map((r, idx) => (
            <tr key={idx}>
              <td>{r.giorno}</td>
              <td>{r.ora}</td>
              <td>{r.classe}</td>
              <td>{r.docente}</td>
              <td>{r.aula}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Orario;

