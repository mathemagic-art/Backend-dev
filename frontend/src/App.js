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
const App = () => {
  return (
    <div className="text-white text-center text-2xl">
      <Home />
    </div>
  );
};

export default App;
>>>>>>> 767bd47bc412ab43bfe5985522c85c1ef47fa2e7
