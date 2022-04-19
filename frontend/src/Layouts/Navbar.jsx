import React from "react";
import NavLink from "../Components/NavLink";
const Navbar = () => {
  return (
    <div>
      <input type={"checkbox"} className="w-10 h-10"></input>
      <NavLink text="Test Yourself" />
      <NavLink text="CheatSheet" />
      <NavLink text="learning Materials" />
    </div>
  );
};

export default Navbar;
