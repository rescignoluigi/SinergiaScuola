import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Disponibilita() {
  const [slots, setSlots] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errore, setErrore] = useState(null);

  useEffect(() => {
    const fetchDisponibilita = async () => {
      try {
        const res = await axios.get('/api/disponibilita');
        setSlots(res.data);
      } catch (err) {
        setErrore('Errore nel caricamento delle disponibilità');
      } finally {
        setLoading(false);
      }
    };
    fetchDisponibilita();
  }, []);

  if (loading) return <p>Caricamento disponibilità…</p>;
  if (errore) return <p className="error">{errore}</p>;

  return (
    <section>
      <h1>Disponibilità docenti</h1>
      <table className="table">
        <thead>
          <tr>
            <th>Docente</th>
            <th>Giorno</th>
            <th>Ora</th>
          </tr>
        </thead>
        <tbody>
          {slots.map((s, idx) => (
            <tr key={idx}>
              <td>{s.docente}</td>
              <td>{s.giorno}</td>
              <td>{s.ora}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default Disponibilita;

