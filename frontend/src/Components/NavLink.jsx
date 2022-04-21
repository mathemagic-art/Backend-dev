import React from "react";
import { Link } from "react-router-dom";

const NavLink = ({ text }) => {
  return (
    <>
      <Link to={"/"+text.replace(" ", "")}>{text}</Link>
    </>
  );
};

export default NavLink;
