import React from "react";
import RouteItem from "../Components/RouteItem";

const FunctionsMenu = () => {
  return (
    <>
      <ul className="w-[30rem] h-full bg-black opacity-90 absolute left-0 top-24">
        <RouteItem text="Newton's Method Calculator" path="newton" />
        <RouteItem text="Derivative Calculator" path="diff" />
        <RouteItem text="Limit Calculator" path="limit" />
      </ul>
    </>
  );
};

export default FunctionsMenu;
