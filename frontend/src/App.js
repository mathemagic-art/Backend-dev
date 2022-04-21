import axios from "axios";
<<<<<<< HEAD

export default class PersonAdd extends React.Component {
  state = {
    equation: "",
    first: null,
    second: null,
    answer: "",
  };

  handleEquation = (event) => {
    this.setState({ equation: event.target.value });
  };
  handleFirst = (event) => {
    this.setState({ first: event.target.value });
  };
  handleSecond = (event) => {
    this.setState({ second: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();

    const user = {
      equation: this.state.equation,
      first: this.state.first,
      second: this.state.second,
    };

    axios.post(`http://127.0.0.1:8001/simpson/`, this.state).then((res) => {
      console.log(res);
      this.setState({ answer: res["data"] });
      console.log(res.data);
    });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Equation:
            <input type="text" name="equation" onChange={this.handleEquation} />
          </label>
          <label>
            First:
            <input type="number" name="first" onChange={this.handleFirst} />
          </label>
          <label>
            Second:
            <input type="number" name="second" onChange={this.handleSecond} />
          </label>
          <button type="submit">Add</button>
        </form>
        <div>
          {this.state.answer !== "" ? "The answer is " + this.state.answer : ""}
        </div>
      </div>
    );
  }
}
=======
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
>>>>>>> 767bd47bc412ab43bfe5985522c85c1ef47fa2e7
