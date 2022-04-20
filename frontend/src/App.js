import React from "react";
import axios from "axios";

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
