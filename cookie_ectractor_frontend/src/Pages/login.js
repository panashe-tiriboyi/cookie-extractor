import React, { Component } from "react";
import "../components/login.css";
import axios from "axios";
import { Empty, Button, message } from "antd";

export default class Login extends React.Component {
  state = {
    credentials: { username: "", password: "" },
  };

  headers = {
    headers: {
      "Content-Type": "application/json",
    },
    mode: "cors",
  };

  open = () => {
    const win = window.open(URL, "/");
    if (win != null) {
      win.focus();
    }
  };

  login = (event) => {
    // send post request with credentials to backend
    var post_data = this.state.credentials;
    //post_data = JSON.stringify({ post_data });

    const endpoint = "http://127.0.0.1:8000/auth/";

    if (post_data.username === "" || post_data.password === "") {
      message.warn(" enter username and password");
    } else {
      axios
        .post(endpoint, post_data, this.headers)
        .then((res) => {
          if (res.status === 200) {
            message.success(
              ` ${post_data.username} has successfully logged in.`
            );
            console.log(res.data);
            this.props.handleLogin();
          }
        })
        .catch((error) => {
          console.log("failed to post to db");

          if (error.response.data.non_field_errors[0]) {
            console.log(error.response.data.non_field_errors[0]);
            message.warn(`${error.response.data.non_field_errors[0]}`);
          } else if (error.response.data.password[0]) {
            console.log(error.response.data.password[0]);
            message.warn(`${error.response.data.password[0]}`);
          } else if (error.response.data.password[0]) {
            console.log(error.response.data.username[0]);
            message.warn(`${error.response.data.username[0]}`);
          } else {
            console.log(error);
          }

          //console.log(error.response.data.non_field_errors[0]);
        });
    }
  };

  inputChanged = (event) => {
    const cred = this.state.credentials;
    cred[event.target.name] = event.target.value;
    this.setState({ credentials: cred });
    console.log(this.state.credentials);
  };

  render() {
    return (
      <div className="login">
        <h1>Login User</h1>

        <input
          name="username"
          className="userInput"
          placeholder="Enter Username"
          type="text"
          onChange={this.inputChanged}
        />
        <br />
        <input
          name="password"
          className="userInput"
          placeholder="Password"
          type="password"
          onChange={this.inputChanged}
        />
        <br />
        <button className="btn" onClick={this.login}>
          Login
        </button>
      </div>
    );
  }
}
