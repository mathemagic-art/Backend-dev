import axios from "axios";
import "./App.css";
import Home from "./Pages/Home";
import Test from "./Pages/Test.jsx";
import { Route, Routes } from "react-router-dom";
import NewtonMethod from "./Pages/NewtonMethod";

const App = () => {
  return (
    <Routes>
      <Route exact path="/" element={<Home />}></Route>
      <Route path="/TEST" element={<Test />}></Route>
      <Route path="/Newton" element={<NewtonMethod />}></Route>
    </Routes>
  );
};

export default App;
