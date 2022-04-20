import { useState } from "react";
import Hero from "../Layouts/Hero";
import Navbar from "../Layouts/Navbar";

const Home = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  };
  return (
    <div>
      <Navbar />
      <Hero />
    </div>
  );
};

export default Home;
