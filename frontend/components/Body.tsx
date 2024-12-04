import React from "react";
import logo from '../assets/images/logo.png';
import './Body.css';
const Body = () => {
  return(
  <div className="body">
    <h1>Welcome to</h1>
    <img src={logo} className="logo" />
  </div>
  )
};

export default Body;
