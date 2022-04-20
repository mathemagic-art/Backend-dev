import axios from "axios";
import "./App.css";
import Home from "./Pages/Home";
import Test from "./Pages/Test.jsx";
import { Route, Router, Routes } from "react-router-dom";
const App = () => {
  return (
    <Routes>
      <Route exact path="/" element={<Home />}></Route>
      <Route path="/TEST" element={<Test />}></Route>
    </Routes>
  );
};

export default App;
