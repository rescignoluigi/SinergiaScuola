import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Assenze() {
  const [assenze, setAssenze] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const fetchAssenze = async () => {
      try {
        const res = await axios.get('/api/assenze');
        setAssenze(res.data);
      } catch (err) {
        setErrore('Errore nel caricamento delle assenze');
      } finally {
        setLoading(false);
      }
    };
    fetchAssenze();
  }, []);

  if (loading) return <p>Caricamento assenze…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Assenze</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Data</th>
            <th>Classe</th>
            <th>Alunno</th>
            <th>Motivo</th>
          </tr>
        </thead>
        <tbody>
          {assenze.map((a, idx) => (
            <tr key={idx}>
              <td>{a.data}</td>
              <td>{a.classe}</td>
              <td>{a.alunno}</td>
              <td>{a.motivo}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Assenze;

