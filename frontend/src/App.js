import axios from "axios";
import "./App.css";
import Home from "./Pages/Home";
import TEST_YOURSELF from "./Pages/TEST_YOURSELF";
import { Route, Routes } from "react-router-dom";
import NewtonMethod from "./Pages/NewtonMethod";
import CHEATSHEETS from "./Pages/CHEATSHEETS";
import LEARNING_MATERIALS from "./Pages/LEARNING_MATERIALS";
import ABOUT from "./Pages/About";

const App = () => {
  return (
    <Routes>
      <Route exact path="/" element={<Home />}></Route>
      <Route path="/TESTYOURSELF" element={<TEST_YOURSELF />}></Route>
      <Route path="/Newton" element={<NewtonMethod />}></Route>
      <Route path="/CHEATSHEETS" element={<CHEATSHEETS />}></Route>
      <Route path="/LEARNINGMATERIALS" element={ <LEARNING_MATERIALS />}></Route>
      <Route path="/ABOUT" element={<ABOUT />}></Route>
    </Routes>
  );
};

export default App;
