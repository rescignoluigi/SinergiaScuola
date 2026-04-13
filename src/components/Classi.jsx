import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Classi() {
  const [classi, setClassi] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const fetchClassi = async () => {
      try {
        const res = await axios.get('/api/classi');
        setClassi(res.data);
      } catch (err) {
        setErrore('Errore nel caricamento delle classi');
      } finally {
        setLoading(false);
      }
    };
    fetchClassi();
  }, []);

  if (loading) return <p>Caricamento classi…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Classi</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Plesso</th>
            <th>Anno</th>
            <th>Sezione</th>
          </tr>
        </thead>
        <tbody>
          {classi.map((c) => (
            <tr key={c.id}>
              <td>{c.plesso_nome || c.plesso}</td>
              <td>{c.anno}</td>
              <td>{c.sezione}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Classi;

