import React from 'react';
import { NavLink } from 'react-router-dom';

function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-title">SinergiaScuola</div>
      <nav className="navbar-links">
        <NavLink to="/plessi" className="nav-link">Plessi</NavLink>
        <NavLink to="/classi" className="nav-link">Classi</NavLink>
        <NavLink to="/docenti" className="nav-link">Docenti</NavLink>
        <NavLink to="/orario" className="nav-link">Orario</NavLink>
        <NavLink to="/assenze" className="nav-link">Assenze</NavLink>
        <NavLink to="/disponibilita" className="nav-link">Disponibilità</NavLink>
      </nav>
    </header>
  );
}

export default Navbar;

