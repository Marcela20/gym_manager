import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import GroupList from "./GroupList";
import NewGroupModal from "./NewGroupModal";



import axios from "axios";

import { API_GROUP_URL } from ".";


class GroupDom extends Component {
  state = {
    groups: []
  };

  componentDidMount() {
    this.resetState();
  }

  getGroups = () => {
    axios.get(API_GROUP_URL).then(res => this.setState({ groups: res.data }));
  };

  resetState = () => {
    this.getGroups();
  };
  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <GroupList
              groups={this.state.groups}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewGroupModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default GroupDom;
