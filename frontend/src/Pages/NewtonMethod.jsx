import { useState } from "react";
import MethodsCard from "../Components/MethodsCard";
import Navbar from "../Layouts/Navbar";
import { ReactComponent as Fx } from "../Files/svgs/fx.svg";
import FunctionsMenu from "../Layouts/FunctionsMenu";

const NewtonMethod = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <Navbar toggle={toggle} />
      {isOpen ? <FunctionsMenu /> : ""} 
      <div className="ml-32 mt-20 border-2 w-1/3 rounded-lg text-white p-10 bg-dark bg-opacity-30">
        <h2 className="text-center text-3xl font-primary text-primary">
          Newton's Method Calculator
        </h2>
        <p className="text-center text-text mb-10">
          Finds the roots of the equation f(x)=0{" "}
        </p>
        <div>
          <label htmlFor="function" className="ml-2 text-bright">
            Enter a function f(x)
          </label>
          <div className="flex rounded-xl text-black mb-10" id="searchbox">
            <input
              className="w-full p-4 border-2  border-primary rounded-l-xl"
              type="text"
              id="function"
            />{" "}
            <button className="px-4 border-2 border-primary rounded-r-xl ">
              <Fx />
            </button>
          </div>
          <label htmlFor="figure" className="ml-2 text-bright">
            Significant Figure
          </label>
          <input
            type="text"
            id="figure"
            className="w-full p-4 border-2 text-black  border-primary rounded-xl mb-10"
          />
          <label htmlFor="iteration" className="ml-2 text-bright">
            Number of Iterations
          </label>
          <input
            type="text"
            id="iteration"
            className="w-full p-4 border-2  text-black border-primary rounded-xl mb-10"
          />
        </div>
        <div className=" flex justify-evenly">
          <button className="bg-primary text-white px-6 py-2 text-center text-lg rounded-md">
            Magic!
          </button>
          <button className="bg-white text-black px-6 py-2 text-center text-lg rounded-md">
            Reset!
          </button>
        </div>
      </div>
    </>
  );
};

export default NewtonMethod;
