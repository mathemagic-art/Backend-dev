// import axios from "axios";
import { useState } from "react";
import "./App.css";
import Home from "./Pages/Home";
import TEST_YOURSELF from "./Pages/TEST_YOURSELF";
import { Route, Routes } from "react-router-dom";
import NewtonMethod from "./Pages/NewtonMethod";
import CHEATSHEETS from "./Pages/CHEATSHEETS";
import LEARNING_MATERIALS from "./Pages/LEARNING_MATERIALS";
import ABOUT from "./Pages/About";
import DiffCalculator from "./Pages/DiffCalculator";
import LimitCalc from "./Pages/LimitCalc";
import TaylorCalc from "./Pages/TaylorCalc";
import SimpsonCalc from "./Pages/SimpsonCalc";
import TrapezoidCalc from "./Pages/TrapezoidCalc";
import RectangleCalc from "./Pages/RectangleCalc";
import DefIntegralCalc from "./Pages/DefIntegralCalc";

const App = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  };
  return (
    <Routes>
      <Route
        exact
        path="/"
        element={<Home toggle={toggle} isOpen={isOpen} />}
      ></Route>
      <Route
        path="/TESTYOURSELF"
        element={<TEST_YOURSELF toggle={toggle} isOpen={isOpen} />}
      ></Route>
      <Route path="/newton" element={<NewtonMethod />}></Route>
      <Route path="/diff" element={<DiffCalculator />}></Route>
      <Route
        path="/CHEATSHEETS"
        element={<CHEATSHEETS toggle={toggle} isOpen={isOpen} />}
      ></Route>
      <Route
        path="/LEARNINGMATERIALS"
        element={<LEARNING_MATERIALS toggle={toggle} isOpen={isOpen} />}
      ></Route>
      <Route
        path="/ABOUT"
        element={<ABOUT toggle={toggle} isOpen={isOpen} />}
      ></Route>
      <Route path="/limit" element={<LimitCalc />}></Route>
      <Route path="/taylor" element={<TaylorCalc />}></Route>
      <Route path="/simpson" element={<SimpsonCalc />}></Route>
      <Route path="/trapezoid" element={<TrapezoidCalc />}></Route>
      <Route path="/rectangle" element={<RectangleCalc />}></Route>
      <Route path="/definite-integral" element={<DefIntegralCalc />}></Route>
    </Routes>
  );
};

export default App;
