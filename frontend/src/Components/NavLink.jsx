import React from "react";
import { Link } from "react-router-dom";

const NavLink = ({ text }) => {
  return (
    <>
      <Link to={"/" + text}>{text}</Link>
    </>
  );
};

export default NavLink;
