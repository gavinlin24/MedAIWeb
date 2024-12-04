import React from "react";
import "./Navbar.css";

import search from "../../assets/images/search.png";
import watermark from "../../assets/images/watermark.png";

const Navbar = () => {
  return (
    <div className="navbar">
      <div>
        <img src={watermark} alt="" className="logo-icon" />
        
      </div>

      <ul>
        <li>Home</li>
        <li>About</li>
      </ul>

      <img src={search} alt="" className="toggle-icon" />
    </div>
  );
};

export default Navbar;
