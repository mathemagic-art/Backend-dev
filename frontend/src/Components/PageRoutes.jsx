import React from "react";
import { Link } from "react-router-dom";

const PagesRoute = ({ text, route }) => {
  return (
    <>
      <Link to={"/" + route.replace(" ", "")}>{text}</Link>
    </>
  );
};

export default PagesRoute;
