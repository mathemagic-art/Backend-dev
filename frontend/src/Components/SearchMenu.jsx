import React from "react";
import { ReactComponent as Placeholder } from "../Files/svgs/Placeholder.svg";
import { ReactComponent as Functions } from "../Files/svgs/functions.svg";
import { ReactComponent as Fx } from "../Files/svgs/ButtonFx.svg";
import { ReactComponent as Search } from "../Files/svgs/search.svg";

const SearchMenu = () => {
  return (
    <div className="flex flex-col w-1/3 m-auto justify-center items-center bg-transparent mt-10">
      <div className="flex justify-center items-center border-2">
        <Placeholder />
        <input type="text" className="bg-black py-4 inline-block " />
        <Fx />
        <button className="px-4">
          <Search />
        </button>
      </div>
      <div className="bg-black bg-opacity-80 z-10 rounded-3xl">
        <Functions />
      </div>
    </div>
  );
};

export default SearchMenu;
