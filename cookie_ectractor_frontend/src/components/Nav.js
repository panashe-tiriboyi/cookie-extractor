import React from "react";
import "../nav.css";
import { Link } from "react-router-dom";

function Nav() {
  return (
    <>
      <nav className="navbar">
        <div className="logo">COOKIE EXTRATOR</div>

        <ul className="nav-links">
          <div className="menu">
            <Link to="/">
              <button className="bttn">Home</button>
            </Link>
            <Link to="/login">
              <button className="bttn">Login</button>
            </Link>
            <Link to="/register">
              <button className="bttn">Register</button>
            </Link>
          </div>
        </ul>
      </nav>
    </>
  );
}

export default Nav;
