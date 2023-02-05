import React, { Component } from "react";
import "./login.css";
import axios from "axios";
import { Empty, Button, message } from "antd";

export default class Register extends Component {
  state = {
    credentials: { email: "", username: "", password: "", confirmPassword: "" },
  };

  headers = {
    headers: {
      "Content-Type": "application/json",
    },
    mode: "cors",
  };

  login = (event) => {
    // send post request with credentials to backend

    var post_data = {
      email: this.state.credentials.email,
      username: this.state.credentials.username,
      password: this.state.credentials.password,
    };

    const endpoint = "http://127.0.0.1:8000/accounts/users/";
    if (post_data.password === this.state.credentials.password) {
      axios
        .post(endpoint, post_data, this.headers)
        .then((res) => {
          if (res.status === 201) {
            message.success(
              `User successfully registered ${post_data.username}`
            );
          }
        })
        .catch((error) => {
          console.log("failed to post to db");
          console.log(error);
        });
    } else {
      message.warn("Password do not match");
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
        <h1>Register User</h1>
        <br />
        <input
          name="email"
          className="userInput"
          placeholder="Enter Email"
          type="text"
          onChange={this.inputChanged}
        />
        <br />
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
        <input
          name="confirmPassword"
          className="userInput"
          placeholder="Confirm Password"
          type="password"
          onChange={this.inputChanged}
        />
        <br />
        <button className="btn" onClick={this.login}>
          Register
        </button>
      </div>
    );
  }
}
