import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import InstructorList from "./InstructorList";
import NewInstructorModal from "./NewInstructorModal";



import axios from "axios";

import { API_INSTRUCTOR_URL } from ".";


class InstructorDom extends Component {
  state = {
    instructors: []
  };

  componentDidMount() {
    this.resetState();
  }

  getInstructors = () => {
    axios.get(API_INSTRUCTOR_URL).then(res => this.setState({ instructors: res.data }));
  };

  resetState = () => {
    this.getInstructors();
  };
  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <InstructorList
              instructors={this.state.instructors}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewInstructorModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default InstructorDom;
