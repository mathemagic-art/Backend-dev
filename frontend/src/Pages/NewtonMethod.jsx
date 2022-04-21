import { useState } from "react";
import Navbar from "../Layouts/Navbar";

const NewtonMethod = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <Navbar toggle={toggle} />
    </>
  );
};

export default NewtonMethod;