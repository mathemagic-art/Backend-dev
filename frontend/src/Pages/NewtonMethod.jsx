import axios from "axios"
import { useState, useEffect } from "react";
// import MethodsCard from "../Components/MethodsCard";
import Navbar from "../Layouts/Navbar";
import { ReactComponent as Fx } from "../Files/svgs/fx.svg";
import FunctionsMenu from "../Layouts/FunctionsMenu";

const NewtonMethod = () => {
  const [data, setData] = useState({})
  const [answer, setAnswer] = useState("")
  const [isOpen, setIsOpen] = useState(false);

  const handleInput = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setData(values => ({...values, [name]: value}))
  }

  console.log(data)

  // const handleInput = (event) => {
  //   console.log(event.target)
  //   setData(values => ({...values, [event.target.name] : event.target.value}))

  // }
  // const handleFunction = (event) => {
  //   // setData({equation: event.target.value});
  //   // console.log("samat")
  // };
  // const handleFirst = (event) => {
  //   setData({first: event.target.value})
  // };
  // const handleSecond = (event) => {
  //   setData({second: event.target.value})
    
  // };

  // const handleClick = () =>{
  //   console.log(data)
  //   // axios.post("http://127.0.0.1:8000/newton/", data).then((res)=>{setAnswer(res)})
  // };

  const handleReset = (event) => {
    event.preventDefault()
    setData({equation:"", first:"", second:""})
  }

  // useEffect(() => {
    
  // }, [data, setData])
  
  
  console.log(answer)
  
  const toggle = () => {
    setIsOpen(!isOpen);
  };
  
  const handleSubmit = (event) => {
    axios.post("http://127.0.0.1:8000/newton/", data).then((res)=>{setAnswer(res.data)})
    console.log(data)
    console.log(answer)
    event.preventDefault()
    
  }
  return (
    <>
      <Navbar toggle={toggle} />
      {isOpen ? <FunctionsMenu /> : ""} 
      <form onSubmit={handleSubmit}>
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
              // id="function"
              name="equation"
              value={data.equation}
              onChange={handleInput}

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
            // id="figure"
            name="first"
            value={data.first}
            onChange={handleInput}
            className="w-full p-4 border-2 text-black  border-primary rounded-xl mb-10"
          />
          <label htmlFor="iteration" className="ml-2 text-bright">
            Number of Iterations
          </label>
          <input
            type="text"
            // id="iteration"
            value={data.second}
            name="second"
            onChange={handleInput}
            className="w-full p-4 border-2  text-black border-primary rounded-xl mb-10"
          />
        </div>
        <div className=" flex justify-evenly">
          <button className="bg-primary text-white px-6 py-2 text-center text-lg rounded-md" type="submit" >
            Magic!
          </button>
          <button className="bg-white text-black px-6 py-2 text-center text-lg rounded-md" onClick={handleReset}>
            Reset!
          </button>
        </div>
      </div>
      <div style={{ backgroundColor:"white"}}>
        {answer !=="" ? answer:"No Answer" }
      </div>
      </form>
    </>
  );
};

export default NewtonMethod;
