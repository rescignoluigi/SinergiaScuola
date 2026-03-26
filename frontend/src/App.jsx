import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar.jsx';
import Plessi from './components/Plessi.jsx';
import Classi from './components/Classi.jsx';
import Docenti from './components/Docenti.jsx';
import Orario from './components/Orario.jsx';
import Assenze from './components/Assenze.jsx';
import Disponibilita from './components/Disponibilita.jsx';

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Navigate to="/plessi" replace />} />
          <Route path="/plessi" element={<Plessi />} />
          <Route path="/classi" element={<Classi />} />
          <Route path="/docenti" element={<Docenti />} />
          <Route path="/orario" element={<Orario />} />
          <Route path="/assenze" element={<Assenze />} />
          <Route path="/disponibilita" element={<Disponibilita />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;

