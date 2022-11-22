import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Student_DOM from "./components/Student_DOM";
import Instructor_DOM from "./components/Instructor_DOM";
import Group_DOM from  "./components/Group_DOM";
import Calendar from "./components/calendar";
class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <h4 className="text-center">students</h4>
        <Student_DOM />
        <h4 className="text-center">instructors</h4>
        <Instructor_DOM />
        <Group_DOM />
        <Calendar />


      </Fragment>
    );
  }
}

export default App;