import React from "react";
import { Link } from 'react-router-dom';
import {
  BrowserRouter as Router, 
  Routes, 
  Route
} from 'react-router-dom';
const NavLink = ({ text }) => {
  return (
    <>
      <Router>
          <Link to={"/"+text}>{text}</Link>
          <Routes>
            <Route path="/" />
            <Route path={"/"+text} />
        </Routes>
    </Router>
    </>
  );
};

export default NavLink;
