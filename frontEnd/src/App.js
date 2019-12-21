import React, { Component } from "react";
import List from "./components/List";
import axios from "axios";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { courses: [] };
  }
  componentDidMount() {
    axios
      .get("https://catalog-api.udacity.com/v1/degrees")
      .then(response => {
        /// avaliable and open for enrollment
        const courses = response.data.degrees.filter(course => {
          return (
            course["available"] === true &&
            course["open_for_enrollment"] === true
          );
        });

        this.setState({
          courses: courses
        });
      })
      .catch(function(error) {
        console.log(error);
      });
  }

  render() {
    return <List courses={this.state.courses} />;
  }
}

export default App;
