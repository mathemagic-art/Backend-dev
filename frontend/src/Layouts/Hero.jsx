import React from "react";
import SearchMenu from "../Components/SearchMenu";
import { ReactComponent as HeroBg } from "../Files/svgs/HeroBG.svg";

const Hero = () => {
  return (
    <div className="w-3/4 flex flex-col items-center mt-52 mx-auto">
      <h1 className="text-white text-4xl  tracking-wide">
        Creative solutions for <br /> brilliant minds
      </h1>
      <SearchMenu />
      <HeroBg className="-mt-44" />
    </div>
  );
};

export default Hero;
