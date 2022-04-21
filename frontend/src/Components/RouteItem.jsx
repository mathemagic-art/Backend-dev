import React from "react";
import { Link } from "react-router-dom";
import { ReactComponent as Fx } from "../Files/svgs/fx.svg";

const RouteItem = ({ text, path }) => {
  return (
    <>
      <li className="w-full p-5 pt-7 text-white font-primary text-2xl">
        <Link to={"/" + path} className="flex ">
          <Fx className="mr-4" />
          {text}
        </Link>
      </li>
    </>
  );
};

export default RouteItem;
