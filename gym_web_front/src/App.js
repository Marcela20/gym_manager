import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import StudentDom from "./components/Student_DOM";
import InstructorDom from "./components/Instructor_DOM";
import GroupDom from  "./components/Group_DOM";
import Calendar from "./components/calendar_new";
import Table from "./components/Table_flex";


class App extends Component {

  render() {
    return (
      <Fragment>
        <Header />
        <h4 className="text-center">students</h4>
        <StudentDom />
        <h4 className="text-center">instructors</h4>
        <InstructorDom />
        <h4 className="text-center">groups</h4>
        <GroupDom />
        <Calendar />
        <Table />
      </Fragment>
    );

  }
}

export default App;

