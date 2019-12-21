import React, { Component } from "react";
import Axios from "axios";

export default class ListItem extends Component {
  render() {
    function setEnrollment(id) {
      Axios.post("http://127.0.0.1:5000/enrollment", {
        nanodegree_key: id
      }).then(res => console.log(res));
    }
    return (
      <li>
        <button onClick={() => setEnrollment(this.props.id)}>enroll</button>
        <a
          target="_blank"
          href={"https://catalog-api.udacity.com/v1/degrees/" + this.props.id}
        >
          {this.props.title}
        </a>
      </li>
    );
  }
}
