import { useState } from "react";
import { ReactComponent as Placeholder } from "../Files/svgs/Placeholder.svg";
import { ReactComponent as Functions } from "../Files/svgs/functions.svg";
import { ReactComponent as Fx } from "../Files/svgs/ButtonFx.svg";
import { ReactComponent as Search } from "../Files/svgs/search.svg";

const SearchMenu = () => {
  const [functionsOpen, setFunctionsOpen] = useState(true);

  const toggleFunctions = () => {
    setFunctionsOpen(!functionsOpen);
  };
  return (
    <div className="flex flex-col m-auto justify-center bg-transparent mt-10 laptop:-mt-6 laptop:pt-20 text-white text-xl mb-52 z-10 w-2/3">
      <div className="flex justify-center items-center border-2 rounded-lg border-blue-500">
        <Placeholder />
        <input type="text" className="bg-black py-4 inline-block w-2/3" />
        <button onClick={toggleFunctions}>
          <Fx />
        </button>
        <button className="px-4 py-4">
          <Search />
        </button>
      </div>
      <div className="bg-black bg-opacity-80 z-10 rounded-3xl tablet:mr-20  mt-5 absolute top-2/4">
        {functionsOpen ? <Functions className="w-full" /> : ""}
      </div>
    </div>
  );
};

export default SearchMenu;
