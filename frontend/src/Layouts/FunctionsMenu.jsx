import React from "react";
import RouteItem from "../Components/RouteItem";

const FunctionsMenu = () => {
  return (
    <>
      <ul className="w-[30rem] h-full bg-black opacity-90 absolute left-0 top-24">
        <RouteItem text="Newton's Method Calculator" path="Newton" />
      </ul>
    </>
  );
};

export default FunctionsMenu;
