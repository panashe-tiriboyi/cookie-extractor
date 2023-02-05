import "./App.css";

import { BrowserRouter, Router, Routes, Route, Link } from "react-router-dom";
import Users from "./Pages/Users";
import Table from "./Pages/Table";
import Nav from "./components/Nav";
import Login from "./Pages/login.js";
import { useEffect, useState } from "react";
let isFirst = window.sessionStorage.setItem("isFirst", JSON.stringify(true));

function App() {
  if (isFirst) {
    window.sesionStorage.setItem("isFirst", JSON.stringify(false));
    window.sessionStorage.setItem("USER_LOGGED_STATUS", JSON.stringify(false));
  }
  const [isLoggedIn, setisLoggedIn] = useState(
    JSON.parse(window.sessionStorage.getItem("USER_LOGGED_STATUS")) === true
      ? true
      : false
  );

  const handleLogin = () => {
    setisLoggedIn(true);
  };

  useEffect(() => {
    window.sessionStorage.setItem(
      "USER_LOGGED_STATUS",
      JSON.stringify(isLoggedIn)
    );
  }, [isLoggedIn]);

  return (
    <BrowserRouter>
      <div className="App">
        <Nav />
        <Routes>
          {isLoggedIn ? (
            <Route path="/" element={<Table isLoggedIn={isLoggedIn} />} />
          ) : (
            <Route
              path="/"
              element={
                <div className="logInFirst">
                  <h2> Log in first to enter Domain</h2>
                </div>
              }
            />
          )}
          <Route path="/register" element={<Users />} />
          <Route path="/login" element={<Login handleLogin={handleLogin} />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
