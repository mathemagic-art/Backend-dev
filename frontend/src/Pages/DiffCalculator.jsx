import axios from "axios";
import { useState } from "react";
// import MethodsCard from "../Components/MethodsCard";
import Navbar from "../Layouts/Navbar";
import { ReactComponent as Fx } from "../Files/svgs/fx.svg";
import { ReactComponent as Newton } from "../Files/svgs/newtonwhite.svg";
import { ReactComponent as X2 } from "../Files/svgs/xSquare.svg";
import FunctionsMenu from "../Layouts/FunctionsMenu";

const DiffCalculator = () => {
  const [data, setData] = useState({argument_1: "", argument_2: "x", argument_3:"1"});
  const [answer, setAnswer] = useState("");
  const [isOpen, setIsOpen] = useState(false);

  const handleInput = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setData((values) => ({ ...values, [name]: value }));
  };

  console.log(data);



  // const handleInput = (event) => {
  //   console.log(event.target)
  //   setData(values => ({...values, [event.target.name] : event.target.value}))

  // }
  // const handleFunction = (event) => {
  //   // setData({equation: event.target.value});
  //   // console.log("samat")
  // };
 
  // const handleSecond = (event) => {
  //   setData({second: event.target.value})

  // };

  // const handleClick = () =>{
  //   console.log(data)
  //   // axios.post("http://127.0.0.1:8000/diff/", data).then((res)=>{setAnswer(res)})
  // };

  const handleReset = (event) => {
    event.preventDefault();
    setData({ argument_1: "", argument_2: 'x', argument_3: '1' });
    setAnswer("");
  };


  let variable = "f("+(data.argument_2)+")"
  // useEffect(() => {

  // }, [data, setData])

  console.log(answer);

  const toggle = () => {
    setIsOpen(!isOpen);
  };

  const handleSubmit = (event) => {
      axios.post("http://127.0.0.1:8000/differentiation/", data).then((res)=>{setAnswer(res.data)})
      console.log(data)
      console.log(answer)
      event.preventDefault()
  }
  return (
    <>
      <Navbar toggle={toggle} />
      {isOpen ? <FunctionsMenu /> : ""}
      <div className="flex">
        <form onSubmit={handleSubmit}>
          <div className="ml-32 mt-12 border-2 w-[60%] h-full rounded-3xl text-white p-10 bg-dark bg-opacity-30">
            <h2 className="text-center text-3xl font-primary text-primary">
              Derivative Calculator
            </h2>
            <p className="text-center text-text mb-10">
              Finds the instantaneous rate of change of a function{" "}
            </p>
            <div>
              <label htmlFor="function" className="ml-2 text-bright">
                Enter a function f(x)
              </label>
              <div className="flex rounded-xl text-black mb-10" id="searchbox">
                <input
                required
                className="w-full p-4 border-2  border-primary rounded-l-xl text-xl"
                type="text" 
                name="argument_1" 
                id="function" 
                value={data.argument_1} 
                onChange={(e) => setData((prev) => ({ ...prev, argument_1: e.target.value }))}

                />{" "}
                <button className="px-4 border-2 border-primary rounded-r-xl ">
                  <Fx />
                </button>
            </div>
            <label htmlFor="first" className="ml-2 text-bright">
                With respect to variable
            </label>
            <select name="argument_2" id="first" value={data.argument_2} onChange={(e) => setData((prev) => ({ ...prev, argument_2: e.target.value }))} className="w-full p-4 border-2 text-black text-xl border-primary rounded-xl mb-10">
                <option   value = "x" className="text-2xl">x</option>
                <option  value = "y">y</option>
                <option  value = "z">z</option>
            </select>
            <label htmlFor="second" className="ml-2 text-bright">
                Order of derivative
            </label>
            <select name="argument_3" id="second" value={data.argument_3} onChange={(e) => setData((prev) => ({ ...prev, argument_3: e.target.value }))} className="w-full p-4 border-2 text-black text-xl border-primary rounded-xl mb-10">
                <option   value = "1" className="text-2xl">First Order</option>
                <option  value = "2">Second Order</option>
            </select>
            </div>
            <div className=" flex justify-evenly">
              <button
                className="bg-primary text-white px-6 py-2 text-center text-lg rounded-md"
                type="submit"
              >
                Magic!
              </button>
              <button
                className="bg-white text-black px-6 py-2 text-center text-lg rounded-md"
                onClick={handleReset}
              >
                Reset!
              </button>
            </div>
          </div>
        </form>
        <div className=" w-1/2 mt-12 mr-20 flex flex-col text-white">
          <p className="mt-24 pl-20 font-normal text-2xl flex">
            According to Differential Rules:
            <Newton className="ml-10 -mt-5" />
          </p>
          <div className="flex mt-10 pl-20 pt-10 h-full w-full flex-row font-normal text-2xl tracking-wide">
            <p>
              The Derivative of{" "}
              {!data.argument_1 ? variable : (variable + " = ") + data.argument_1} equals to{" "}
            </p>
            <div className="ml-3 pt-4 pb-14 border-2 font-normal rounded-xl text-3xl -mt-5 px-3 border-double border-green-600 h-10 bg-white text-black">
              {data.argument_3 === "1" ? "f'" : "f''"}({data.argument_2})={answer !== "" ? answer : "_____________"}
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default DiffCalculator;
