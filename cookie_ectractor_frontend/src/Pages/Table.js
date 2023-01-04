import React, { useEffect, useState } from "react";
import "../table.css";
import { ThreeDots } from "react-loader-spinner";
import { Empty, Button, message } from "antd";
import "antd/dist/antd.min.css"; // or 'antd/dist/antd.less'
import axios from "axios";

function Table(props) {
  const [url, setUrl] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [isCookiePresent, setCookiePresent] = useState(false);
  const [isEmpty, setIsEmpty] = useState(true);
  const [cookie, setCookie] = useState([]);
  const [cookiesFromDB, setCookiesFromDB] = useState([]);
  const [newCookies, setnewCookies] = useState([]);
  const [newTime, setnewTime] = useState();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const headers = {
    headers: {
      "Content-Type": "application/json",
    },
    mode: "cors",
  };

  const handleOnchange = (event) => {
    if (event.key === "Enter") {
      setIsLoading(true);
      setIsEmpty(false);
      setCookiePresent(false);
      console.log(event.target.value);
      const url = event.target.value;
      setUrl(url);

      // send post request with url to backend

      var post_data = {
        cookie_domain: url,
      };

      console.log(post_data);

      const endpoint = "http://127.0.0.1:8000/api/";
      axios
        .post(endpoint, post_data, headers)
        .then((res) => {
          if (res.status === 200) {
            //if post request is succussfull send get request to backend and set cookie
            // show notification

            setIsLoading(false);
            // setCookie(res.data);
            setCookiePresent(true);

            message.success("Domain Sent Successfully");
            const cookie_object = res.data;

            const cookie_batch = [];
            for (let i = 0; i < cookie_object.length; i++) {
              const one_cookie = cookie_object[i];

              cookie_batch.push(one_cookie);
            }

            // get cookies from backend
            const cookies_in_db_url = "http://127.0.0.1:8000/api/db_cookies/";

            axios
              .get(cookies_in_db_url, headers)
              .then((res1) => {
                if (res.status == 200) {
                  setCookiesFromDB(res1.data);
                }
              })
              .catch((error) => {
                setIsLoading(false);
                console.log("failed to get data from db");
                setIsEmpty(true);
                console.log(error);
              });

            setCookie(cookie_batch);
          }
        })
        .catch((error) => {
          setIsLoading(false);
          message.error("Domain took too long to respond");
          setIsEmpty(true);
          console.log(error);
        });
    }
    //comparing the two lists
    console.log(cookiesFromDB);
    //extracting all database cookie names
    const cookieNamesFromeDB = [];
    for (let i = 0; i < cookiesFromDB.length; i++) {
      const one_cookie = cookiesFromDB[i].cookie_name;

      cookieNamesFromeDB.push(one_cookie);
    }
    //Now check which of the new cookies are not in database
    const NewCookies = [];
    var start = new Date().getTime();
    console.log(start);
    for (let i = 0; i < cookie.length; i++) {
      const one_cookie = cookie[i].cookie_name;
      if (cookieNamesFromeDB.includes(one_cookie)) {
        // this cookie exists in DB
        continue;
      } else {
        // this cookie does not exists in Db
        NewCookies.push(cookie[i]);
        console.log(one_cookie);
      }
    }
    var diff = new Date().getTime() - start;
    setnewTime(diff);
    setnewCookies(NewCookies);
  };
  const sendNewCookies = () => {
    setIsLoading(true);
    setIsEmpty(false);
    setCookiePresent(false);

    //now  loop through newCookies And send To DB
    for (let i = 0; i < newCookies.length; i++) {
      const post_cookie_url = "http://127.0.0.1:8000/api/db_cookies/";
      //making a payload
      const payLoad = {
        cookie_name: newCookies[i].cookie_name,
        cookie_domain: newCookies[i].cookie_domain,
        cookie_id: newCookies[i].cookie_id,
        cookie_value: newCookies[i].cookie_value.slice(0, 20),
        cookie_expiry_date: newCookies[i].cookie_expiration_date,
      };
      //
      axios
        .post(post_cookie_url, payLoad, headers)
        .then((res1) => {
          if (res1.status == 201) {
            console.log(res1.data);
            setIsLoading(false);
            // setCookie(res.data);
            setCookiePresent(false);

            setIsEmpty(true);
            message.success("Cookie Saved Successfully");
          }
        })
        .catch((error) => {
          setIsLoading(false);
          // message.error("Domain took too long to respond");
          // setIsEmpty(true);
          console.log(error);
        });
    }
  };
  return (
    <>
      <div class="container">
        <div>
          <h2>{newTime}</h2>
        </div>

        <div class="wrapper">
          <img
            class="search-icon"
            alt=""
            src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDU2Ljk2NiA1Ni45NjYiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDU2Ljk2NiA1Ni45NjY7IiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iMTZweCIgaGVpZ2h0PSIxNnB4Ij4KPHBhdGggZD0iTTU1LjE0Niw1MS44ODdMNDEuNTg4LDM3Ljc4NmMzLjQ4Ni00LjE0NCw1LjM5Ni05LjM1OCw1LjM5Ni0xNC43ODZjMC0xMi42ODItMTAuMzE4LTIzLTIzLTIzcy0yMywxMC4zMTgtMjMsMjMgIHMxMC4zMTgsMjMsMjMsMjNjNC43NjEsMCw5LjI5OC0xLjQzNiwxMy4xNzctNC4xNjJsMTMuNjYxLDE0LjIwOGMwLjU3MSwwLjU5MywxLjMzOSwwLjkyLDIuMTYyLDAuOTIgIGMwLjc3OSwwLDEuNTE4LTAuMjk3LDIuMDc5LTAuODM3QzU2LjI1NSw1NC45ODIsNTYuMjkzLDUzLjA4LDU1LjE0Niw1MS44ODd6IE0yMy45ODQsNmM5LjM3NCwwLDE3LDcuNjI2LDE3LDE3cy03LjYyNiwxNy0xNywxNyAgcy0xNy03LjYyNi0xNy0xN1MxNC42MSw2LDIzLjk4NCw2eiIgZmlsbD0iIzAwMDAwMCIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K"
          />
          <input
            class="search"
            placeholder=" Enter website url "
            type="text"
            onKeyDown={handleOnchange}
          />
          <img
            class="clear-icon"
            alt=""
            src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDUxLjk3NiA1MS45NzYiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxLjk3NiA1MS45NzY7IiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iMTZweCIgaGVpZ2h0PSIxNnB4Ij4KPGc+Cgk8cGF0aCBkPSJNNDQuMzczLDcuNjAzYy0xMC4xMzctMTAuMTM3LTI2LjYzMi0xMC4xMzgtMzYuNzcsMGMtMTAuMTM4LDEwLjEzOC0xMC4xMzcsMjYuNjMyLDAsMzYuNzdzMjYuNjMyLDEwLjEzOCwzNi43NywwICAgQzU0LjUxLDM0LjIzNSw1NC41MSwxNy43NCw0NC4zNzMsNy42MDN6IE0zNi4yNDEsMzYuMjQxYy0wLjc4MSwwLjc4MS0yLjA0NywwLjc4MS0yLjgyOCwwbC03LjQyNS03LjQyNWwtNy43NzgsNy43NzggICBjLTAuNzgxLDAuNzgxLTIuMDQ3LDAuNzgxLTIuODI4LDBjLTAuNzgxLTAuNzgxLTAuNzgxLTIuMDQ3LDAtMi44MjhsNy43NzgtNy43NzhsLTcuNDI1LTcuNDI1Yy0wLjc4MS0wLjc4MS0wLjc4MS0yLjA0OCwwLTIuODI4ICAgYzAuNzgxLTAuNzgxLDIuMDQ3LTAuNzgxLDIuODI4LDBsNy40MjUsNy40MjVsNy4wNzEtNy4wNzFjMC43ODEtMC43ODEsMi4wNDctMC43ODEsMi44MjgsMGMwLjc4MSwwLjc4MSwwLjc4MSwyLjA0NywwLDIuODI4ICAgbC03LjA3MSw3LjA3MWw3LjQyNSw3LjQyNUMzNy4wMjIsMzQuMTk0LDM3LjAyMiwzNS40NiwzNi4yNDEsMzYuMjQxeiIgZmlsbD0iIzAwMDAwMCIvPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo="
          />
        </div>

        {isLoading ? (
          <div className="listner">
            <ThreeDots
              height="80"
              width="80"
              radius="9"
              color="#127850"
              ariaLabel="three-dots-loading"
            />
          </div>
        ) : null}
        {isCookiePresent ? (
          <div class="table-1">
            <h2>New Cookies</h2>

            <table>
              <tbody>
                <tr>
                  <th>Name</th>
                  <th>Value</th>
                  <th>Http Flag</th>
                  <th>Domain</th>
                  <th>Secure Flag</th>
                  <th>Expires</th>
                </tr>

                {newCookies.map((val) => (
                  <tr>
                    <td data-th="Block">{val.cookie_name}</td>
                    <td data-th="Element">{val.cookie_value.slice(0, 20)}</td>
                    <td data-th="Modifier">{val.cookie_http_only_flag}</td>
                    <td data-th="Modifier">{val.cookie_domain}</td>
                    <td data-th="Modifier">{val.cookie_secure_flag}</td>
                    <td data-th="Modifier">{val.cookie_expiration_date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <button
              type="button"
              class="btn btn-success"
              onClick={sendNewCookies}
            >
              Save Cookies
            </button>
          </div>
        ) : null}
        {isEmpty ? (
          <div className="empty">
            <Empty
              description={
                <span>Welcome &#128522; ,Enter url to extract Cookies</span>
              }
              image="https://gw.alipayobjects.com/mdn/miniapp_social/afts/img/A*pevERLJC9v0AAAAAAAAAAABjAQAAAQ/original"
              imageStyle={{
                height: 200,
              }}
            />
          </div>
        ) : null}
      </div>
    </>
  );
}

export default Table;
