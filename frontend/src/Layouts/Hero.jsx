import React from "react";
import SearchMenu from "../Components/SearchMenu";
import { ReactComponent as HeroBg } from "../Files/svgs/HeroBG.svg";
import FunctionsMenu from "./FunctionsMenu";

const Hero = ({ isOpen }) => {
  return (
    <div className="w-3/4 flex flex-col items-center laptop:mt-52 mt-40 mx-auto">
      <h1 className="text-white laptop:text-5xl text-3xl  tracking-wide text-center">
        Creative solutions for <br /> brilliant minds
      </h1>
      <SearchMenu className="h-10" />
      {isOpen ? <FunctionsMenu /> : ""}
      <HeroBg className="-mt-44" />
    </div>
  );
};

export default Hero;
