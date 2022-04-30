import React from "react";
import Hero from "../Layouts/Hero";
import Navbar from "../Layouts/Navbar";


const Home = ({toggle, isOpen}) => {
  return (
    <div>
      <Navbar toggle={toggle} />
      <Hero isOpen={isOpen} />
    </div>
  );
};

export default Home;
