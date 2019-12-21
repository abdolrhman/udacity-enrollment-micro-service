import React, { Component } from "react";
import ListItem from "./ListItem";

export default class List extends Component {
  render() {
    let courses = this.props.courses.map(data => (
      <ListItem key={data.key} id={data.key} {...data} />
    ));
    return (
      <div>
        <h1>Udacity Course List</h1>
        <ol>{courses}</ol>
      </div>
    );
  }
}
