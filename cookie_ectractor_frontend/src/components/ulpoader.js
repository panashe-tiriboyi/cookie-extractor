import React, { useState, useEffect } from "react";
import axios from "axios";
import "./uploader.css";

const Uploader = (props) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const dataArray = [];

  const fetchCookie = async (value) => {
    props.handleLoading(true);
    setLoading(true);
    setData([]);
    const requests = [];
    let createObj = (propValue) => {
      return { cookie_domain: propValue };
    };

    for (let i = 0; i < value.length; i++) {
      let obj = createObj(value[i]);
      requests.push(obj);
    }
    const endpoint = "http://127.0.0.1:8000/api/";

    try {
      // Make the first request

      for (let i = 0; i < requests.length; i++) {
        await axios
          .post(endpoint, requests[i])
          .then((res) => {
            console.log(res.data);
            dataArray.push(...res.data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
      console.log(dataArray);
      setData(dataArray);
      props.handleData(dataArray);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };
  const handleUpload = (e) => {
    //console.log("file", event.target.file);
    let files = e.target.files[0];

    let reader = new FileReader();
    reader.readAsText(files);

    reader.onload = () => {
      //console.log(reader.result);
      let file = reader.result;
      let urlNames = file.split(/\r\n|\n/);

      fetchCookie(urlNames);
    };
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>
      <input
        className=" "
        type="file"
        name="file"
        onChange={handleUpload}
      ></input>
    </div>
  );
};

export default Uploader;
