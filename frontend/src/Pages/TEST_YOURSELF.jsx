import React from "react";
import FunctionsMenu from "../Layouts/FunctionsMenu";
import Navbar from "../Layouts/Navbar";

const Test_Yourself = ({toggle, isOpen}) => {
  return (
    <div>
      <Navbar toggle={toggle} />
      {isOpen ? <FunctionsMenu /> : ""} 
      <h1 className="text-center text-white text-5xl">This is <span>TEST YOURSELF</span> Page</h1>
    </div>
  );
};

export default Test_Yourself;
